from collections.abc import Iterable
import warnings

from hdmf.utils import docval, getargs, popargs, call_docval_func, get_docval
from hdmf.data_utils import DataChunkIterator, assertEqualShape
from hdmf.utils import get_data_shape

from . import register_class, CORE_NAMESPACE
from .base import TimeSeries
from .core import NWBContainer, NWBDataInterface, MultiContainerInterface
from hdmf.common import DynamicTableRegion
from .device import Device


@register_class('ElectrodeGroup', CORE_NAMESPACE)
class ElectrodeGroup(NWBContainer):
    """
    """

    __nwbfields__ = ('name',
                     'description',
                     'location',
                     'device',
                     'position')

    @docval({'name': 'name', 'type': str, 'doc': 'the name of this electrode'},
            {'name': 'description', 'type': str, 'doc': 'description of this electrode group'},
            {'name': 'location', 'type': str, 'doc': 'description of location of this electrode group'},
            {'name': 'device', 'type': Device, 'doc': 'the device that was used to record from this electrode group'},
            {'name': 'position', 'type': 'array_data',
             'doc': 'stereotaxic position of this electrode group (x, y, z)', 'default': None})
    def __init__(self, **kwargs):
        call_docval_func(super(ElectrodeGroup, self).__init__, kwargs)
        description, location, device, position = popargs('description', 'location', 'device', 'position', kwargs)
        self.description = description
        self.location = location
        self.device = device
        if position and len(position) != 3:
            raise Exception('ElectrodeGroup position argument must have three elements: x, y, z, but received: %s'
                            % position)
        self.position = position


@register_class('ElectricalSeries', CORE_NAMESPACE)
class ElectricalSeries(TimeSeries):
    """
    Stores acquired voltage data from extracellular recordings. The data field of an ElectricalSeries
    is an int or float array storing data in Volts. TimeSeries::data array structure: [num times] [num
    channels] (or [num_times] for single electrode).
    """

    __nwbfields__ = ({'name': 'electrodes', 'required_name': 'electrodes',
                      'doc': 'the electrodes that generated this electrical series', 'child': True},
                     'channel_conversion',
                     'filtering')

    @docval(*get_docval(TimeSeries.__init__, 'name'),  # required
            {'name': 'data', 'type': ('array_data', 'data', TimeSeries),  # required
             'shape': ((None, ), (None, None), (None, None, None)),
             'doc': ('The data values. Can be 1D or 2D. The first dimension must be time. The second dimension '
                     'represents electrodes/channels.')},
            {'name': 'electrodes', 'type': DynamicTableRegion,  # required
             'doc': 'the table region corresponding to the electrodes from which this series was recorded'},
            {'name': 'channel_conversion', 'type': ('array_data', 'data'), 'shape': (None,), 'doc':
             "Channel-specific conversion factor. Multiply the data in the 'data' dataset by these values along the "
             "channel axis (as indicated by axis attribute) AND by the global conversion factor in the 'conversion' "
             "attribute of 'data' to get the data values in Volts, i.e, data in Volts = data * data.conversion * "
             "channel_conversion. This approach allows for both global and per-channel data conversion factors needed "
             "to support the storage of electrical recordings as native values generated by data acquisition systems. "
             "If this dataset is not present, then there is no channel-specific conversion factor, i.e. it is 1 for all"
             " channels.", 'default': None},
            {'name': 'filtering', 'type': str, 'doc':
             "Filtering applied to all channels of the data. For example, if this ElectricalSeries represents "
             "high-pass-filtered data (also known as AP Band), then this value could be 'High-pass 4-pole Bessel "
             "filter at 500 Hz'. If this ElectricalSeries represents low-pass-filtered LFP data and the type of "
             "filter is unknown, then this value could be 'Low-pass filter at 300 Hz'. If a non-standard filter "
             "type is used, provide as much detail about the filter properties as possible.", 'default': None},
            *get_docval(TimeSeries.__init__, 'resolution', 'conversion', 'timestamps', 'starting_time', 'rate',
                        'comments', 'description', 'control', 'control_description'))
    def __init__(self, **kwargs):
        name, electrodes, data, channel_conversion, filtering = popargs('name', 'electrodes', 'data',
                                                                        'channel_conversion', 'filtering', kwargs)
        data_shape = get_data_shape(data, strict_no_data_load=True)
        if (
            data_shape is not None
            and len(data_shape) == 2
            and data_shape[1] != len(electrodes.data)
        ):
            if data_shape[0] == len(electrodes.data):
                warnings.warn("The second dimension of data does not match the length of electrodes, but instead the "
                              "first does. Data is oriented incorrectly and should be transposed.")
            else:
                warnings.warn("The second dimension of data does not match the length of electrodes. Your data may be "
                              "transposed.")

        super(ElectricalSeries, self).__init__(name, data, 'volts', **kwargs)
        self.electrodes = electrodes
        self.channel_conversion = channel_conversion
        self.filtering = filtering


@register_class('SpikeEventSeries', CORE_NAMESPACE)
class SpikeEventSeries(ElectricalSeries):
    """
    Stores "snapshots" of spike events (i.e., threshold crossings) in data. This may also be raw data,
    as reported by ephys hardware. If so, the TimeSeries::description field should describing how
    events were detected. All SpikeEventSeries should reside in a module (under EventWaveform
    interface) even if the spikes were reported and stored by hardware. All events span the same
    recording channels and store snapshots of equal duration. TimeSeries::data array structure:
    [num events] [num channels] [num samples] (or [num events] [num samples] for single
    electrode).
    """

    __nwbfields__ = ()

    @docval(*get_docval(ElectricalSeries.__init__, 'name', 'data'),  # required
            {'name': 'timestamps', 'type': ('array_data', 'data', TimeSeries),  # required
             'doc': 'Timestamps for samples stored in data'},
            *get_docval(ElectricalSeries.__init__, 'electrodes'),  # required
            *get_docval(ElectricalSeries.__init__, 'resolution', 'conversion', 'comments', 'description', 'control',
                        'control_description'))
    def __init__(self, **kwargs):
        name, data, electrodes = popargs('name', 'data', 'electrodes', kwargs)
        timestamps = getargs('timestamps', kwargs)
        if not (isinstance(data, TimeSeries) or isinstance(timestamps, TimeSeries)):
            if not (isinstance(data, DataChunkIterator) or isinstance(timestamps, DataChunkIterator)):
                if len(data) != len(timestamps):
                    raise Exception('Must provide the same number of timestamps and spike events')
            else:
                # TODO: add check when we have DataChunkIterators
                pass
        super(SpikeEventSeries, self).__init__(name, data, electrodes, **kwargs)


@register_class('EventDetection', CORE_NAMESPACE)
class EventDetection(NWBDataInterface):
    """
    Detected spike events from voltage trace(s).
    """

    __nwbfields__ = ('detection_method',
                     'source_electricalseries',
                     'source_idx',
                     'times')

    @docval({'name': 'detection_method', 'type': str,
             'doc': 'Description of how events were detected, such as voltage threshold, or dV/dT threshold, '
             'as well as relevant values.'},
            {'name': 'source_electricalseries', 'type': ElectricalSeries, 'doc': 'The source electrophysiology data'},
            {'name': 'source_idx', 'type': ('array_data', 'data'),
             'doc': 'Indices (zero-based) into source ElectricalSeries::data array corresponding '
                    'to time of event. Module description should define what is meant by time of event '
                    '(e.g., .25msec before action potential peak, zero-crossing time, etc). '
                    'The index points to each event from the raw data'},
            {'name': 'times', 'type': ('array_data', 'data'), 'doc': 'Timestamps of events, in Seconds'},
            {'name': 'name', 'type': str, 'doc': 'the name of this container', 'default': 'EventDetection'})
    def __init__(self, **kwargs):
        detection_method, source_electricalseries, source_idx, times = popargs(
            'detection_method', 'source_electricalseries', 'source_idx', 'times', kwargs)
        super(EventDetection, self).__init__(**kwargs)
        self.detection_method = detection_method
        self.source_electricalseries = source_electricalseries
        self.source_idx = source_idx
        self.times = times
        self.unit = 'seconds'


@register_class('EventWaveform', CORE_NAMESPACE)
class EventWaveform(MultiContainerInterface):
    """
    Spike data for spike events detected in raw data
    stored in this NWBFile, or events detect at acquisition
    """

    __clsconf__ = {
        'attr': 'spike_event_series',
        'type': SpikeEventSeries,
        'add': 'add_spike_event_series',
        'get': 'get_spike_event_series',
        'create': 'create_spike_event_series'
    }


@register_class('Clustering', CORE_NAMESPACE)
class Clustering(NWBDataInterface):
    """
    DEPRECATED in favor of :py:meth:`~pynwb.misc.Units`.
    Specifies cluster event times and cluster metric for maximum ratio of
    waveform peak to RMS on any channel in cluster.
    """

    __nwbfields__ = (
        'description',
        'num',
        'peak_over_rms',
        'times'
    )

    @docval({'name': 'description', 'type': str,
             'doc': 'Description of clusters or clustering, (e.g. cluster 0 is noise, '
                    'clusters curated using Klusters, etc).'},
            {'name': 'num', 'type': ('array_data', 'data'), 'doc': 'Cluster number of each event.', 'shape': (None, )},
            {'name': 'peak_over_rms', 'type': Iterable, 'shape': (None, ),
             'doc': 'Maximum ratio of waveform peak to RMS on any channel in the cluster'
                    '(provides a basic clustering metric).'},
            {'name': 'times', 'type': ('array_data', 'data'), 'doc': 'Times of clustered events, in seconds.',
             'shape': (None,)},
            {'name': 'name', 'type': str, 'doc': 'the name of this container', 'default': 'Clustering'})
    def __init__(self, **kwargs):
        import warnings
        warnings.warn("use pynwb.misc.Units or NWBFile.units instead", DeprecationWarning)
        description, num, peak_over_rms, times = popargs(
            'description', 'num', 'peak_over_rms', 'times', kwargs)
        super(Clustering, self).__init__(**kwargs)
        self.description = description
        self.num = num
        self.peak_over_rms = list(peak_over_rms)
        self.times = times


@register_class('ClusterWaveforms', CORE_NAMESPACE)
class ClusterWaveforms(NWBDataInterface):
    """
    DEPRECATED. `ClusterWaveforms` was deprecated in Oct 27, 2018 and will be removed in a future release.
    Please use the `Units` table to store waveform mean and standard deviation
    e.g. `NWBFile.units.add_unit(..., waveform_mean=..., waveform_sd=...)`


    Describe cluster waveforms by mean and standard deviation for at each sample.
    """

    __nwbfields__ = ('clustering_interface',
                     'waveform_filtering',
                     'waveform_mean',
                     'waveform_sd')

    @docval({'name': 'clustering_interface', 'type': Clustering,
             'doc': 'the clustered spike data used as input for computing waveforms'},
            {'name': 'waveform_filtering', 'type': str,
             'doc': 'filter applied to data before calculating mean and standard deviation'},
            {'name': 'waveform_mean', 'type': Iterable, 'shape': (None, None),
             'doc': 'the mean waveform for each cluster'},
            {'name': 'waveform_sd', 'type': Iterable, 'shape': (None, None),
             'doc': 'the standard deviations of waveforms for each cluster'},
            {'name': 'name', 'type': str, 'doc': 'the name of this container', 'default': 'ClusterWaveforms'})
    def __init__(self, **kwargs):
        import warnings
        warnings.warn("use pynwb.misc.Units or NWBFile.units instead", DeprecationWarning)
        clustering_interface, waveform_filtering, waveform_mean, waveform_sd = popargs(
            'clustering_interface', 'waveform_filtering', 'waveform_mean', 'waveform_sd', kwargs)
        super(ClusterWaveforms, self).__init__(**kwargs)
        self.clustering_interface = clustering_interface
        self.waveform_filtering = waveform_filtering
        self.waveform_mean = waveform_mean
        self.waveform_sd = waveform_sd


@register_class('LFP', CORE_NAMESPACE)
class LFP(MultiContainerInterface):
    """
    LFP data from one or more channels. The electrode map in each published ElectricalSeries will
    identify which channels are providing LFP data. Filter properties should be noted in the
    ElectricalSeries description or comments field.
    """

    __clsconf__ = [
        {'attr': 'electrical_series',
         'type': ElectricalSeries,
         'add': 'add_electrical_series',
         'get': 'get_electrical_series',
         'create': 'create_electrical_series'}]


@register_class('FilteredEphys', CORE_NAMESPACE)
class FilteredEphys(MultiContainerInterface):
    """
    Ephys data from one or more channels that has been subjected to filtering. Examples of filtered
    data include Theta and Gamma (LFP has its own interface). FilteredEphys modules publish an
    ElectricalSeries for each filtered channel or set of channels. The name of each ElectricalSeries is
    arbitrary but should be informative. The source of the filtered data, whether this is from analysis
    of another time series or as acquired by hardware, should be noted in each's
    TimeSeries::description field. There is no assumed 1::1 correspondence between filtered ephys
    signals and electrodes, as a single signal can apply to many nearby electrodes, and one
    electrode may have different filtered (e.g., theta and/or gamma) signals represented.
    """

    __clsconf__ = {
        'attr': 'electrical_series',
        'type': ElectricalSeries,
        'add': 'add_electrical_series',
        'get': 'get_electrical_series',
        'create': 'create_electrical_series'
    }


@register_class('FeatureExtraction', CORE_NAMESPACE)
class FeatureExtraction(NWBDataInterface):
    """
    Features, such as PC1 and PC2, that are extracted from signals stored in a SpikeEvent
    TimeSeries or other source.
    """

    __nwbfields__ = ('description',
                     {'name': 'electrodes', 'child': True},
                     'times',
                     'features')

    @docval({'name': 'electrodes', 'type': DynamicTableRegion,
             'doc': 'the table region corresponding to the electrodes from which this series was recorded'},
            {'name': 'description', 'type': ('array_data', 'data'),
             'doc': 'A description for each feature extracted', 'shape': (None, )},
            {'name': 'times', 'type': ('array_data', 'data'), 'shape': (None, ),
             'doc': 'The times of events that features correspond to'},
            {'name': 'features', 'type': ('array_data', 'data'), 'shape': (None, None, None),
             'doc': 'Features for each channel'},
            {'name': 'name', 'type': str, 'doc': 'the name of this container', 'default': 'FeatureExtraction'})
    def __init__(self, **kwargs):
        # get the inputs
        electrodes, description, times, features = popargs(
            'electrodes', 'description', 'times', 'features', kwargs)

        # Validate the shape of the inputs
        # Validate event times compared to features
        shape_validators = []
        shape_validators.append(assertEqualShape(data1=features,
                                                 data2=times,
                                                 axes1=0,
                                                 axes2=0,
                                                 name1='feature_shape',
                                                 name2='times',
                                                 ignore_undetermined=True))
        # Validate electrodes compared to features
        shape_validators.append(assertEqualShape(data1=features,
                                                 data2=electrodes,
                                                 axes1=1,
                                                 axes2=0,
                                                 name1='feature_shape',
                                                 name2='electrodes',
                                                 ignore_undetermined=True))
        # Valided description compared to features
        shape_validators.append(assertEqualShape(data1=features,
                                                 data2=description,
                                                 axes1=2,
                                                 axes2=0,
                                                 name1='feature_shape',
                                                 name2='description',
                                                 ignore_undetermined=True))
        # Raise an error if any of the shapes do not match
        raise_error = False
        error_msg = ""
        for sv in shape_validators:
            raise_error |= not sv.result
            if not sv.result:
                error_msg += sv.message + "\n"
        if raise_error:
            raise ValueError(error_msg)

        # Initialize the object
        super(FeatureExtraction, self).__init__(**kwargs)
        self.electrodes = electrodes
        self.description = description
        self.times = list(times)
        self.features = features
