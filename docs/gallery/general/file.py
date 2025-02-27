"""
.. _basics:

NWB File Basics
==================

This example will focus on the basics of working with an :py:class:`~pynwb.file.NWBFile` object,
including writing and reading of an NWB file, and giving you an introduction to the basic data types.
Before we dive into code showing how to use an :py:class:`~pynwb.file.NWBFile`, we first provide
a brief overview of the basic concepts of NWB. If you are already familiar with the concepts of
:ref:`timeseries_overview` and :ref:`modules_overview`, then feel free to skip the :ref:`basics_background`
part and go directly to :ref:`basics_nwbfile`.

.. _basics_background:

Background: Basic concepts
--------------------------

In the `NWB Format <https://nwb-schema.readthedocs.io>`_, each experimental session is typically
represented by a separate NWB file. NWB files are represented in PyNWB by :py:class:`~pynwb.file.NWBFile`
objects which provide functionality for creating and retrieving:

 * :ref:`timeseries_overview` datasets, i.e., objects for storing time series data
 * :ref:`modules_overview`, i.e., objects for storing and grouping analyses, and
 * experimental metadata and other metadata related to data provenance.

The following sections describe the :py:class:`~pynwb.base.TimeSeries` and :py:class:`~pynwb.base.ProcessingModules`
classes in further detail.

.. _timeseries_overview:

TimeSeries
^^^^^^^^^^

:py:class:`~pynwb.base.TimeSeries` objects store time series data and correspond to the *TimeSeries* specifications
provided by the `NWB Format`_ . Like the NWB specification, :py:class:`~pynwb.base.TimeSeries` Python objects
follow an object-oriented inheritance pattern, i.e., the class :py:class:`~pynwb.base.TimeSeries`
serves as the base class for all other :py:class:`~pynwb.base.TimeSeries` types, such as,
:py:class:`~pynwb.ecephys.ElectricalSeries`, which itself may have further subtypes, e.g.,
:py:class:`~pynwb.ecephys.SpikeEventSeries`.

.. seealso::

    For your reference, NWB defines the following main :py:class:`~pynwb.base.TimeSeries` subtypes:

    * **Extracellular electrophysiology:**
      :py:class:`~pynwb.ecephys.ElectricalSeries`, :py:class:`~pynwb.ecephys.SpikeEventSeries`

    * **Intracellular electrophysiology:**
      :py:class:`~pynwb.icephys.PatchClampSeries` is the base type for all intracellular time series, which
      is further refined into subtypes depending on the type of recording:
      :py:class:`~pynwb.icephys.CurrentClampSeries`,
      :py:class:`~pynwb.icephys.IZeroClampSeries`,
      :py:class:`~pynwb.icephys.CurrentClampStimulusSeries`,
      :py:class:`~pynwb.icephys.VoltageClampSeries`,
      :py:class:`~pynwb.icephys.VoltageClampStimulusSeries`.

    * **Optical physiology and imaging:** :py:class:`~pynwb.image.ImageSeries` is the base type
      for image recordings and is further refined by the
      :py:class:`~pynwb.image.ImageMaskSeries`,
      :py:class:`~pynwb.image.OpticalSeries`, and
      :py:class:`~pynwb.ophys.TwoPhotonSeries` types.
      Other related time series types are:
      :py:class:`~pynwb.image.IndexSeries` and
      :py:class:`~pynwb.ophys.RoiResponseSeries`.

    * **Others** :py:class:`~pynwb.ogen.OptogeneticSeries`,
      :py:class:`~pynwb.behavior.SpatialSeries`,
      :py:class:`~pynwb.misc.DecompositionSeries`,
      :py:class:`~pynwb.misc.AnnotationSeries`,
      :py:class:`~pynwb.misc.AbstractFeatureSeries`, and
      :py:class:`~pynwb.misc.IntervalSeries`.


.. _modules_overview:

Processing Modules
^^^^^^^^^^^^^^^^^^

Processing modules are objects that group together common analyses done during processing of data.
Processing module objects are unique collections of analysis results. To standardize the storage of
common analyses, NWB provides the concept of an :py:class:`~pynwb.core.NWBDataInterface`, where the output of
common analyses are represented as objects that extend the :py:class:`~pynwb.core.NWBDataInterface` class.
In most cases, you will not need to interact with the :py:class:`~pynwb.core.NWBDataInterface` class directly.
More commonly, you will be creating instances of classes that extend this class.


.. seealso::

    For your reference, NWB defines the following main analysis :py:class:`~pynwb.core.NWBDataInterface` subtypes:

    * **Behavior:** :py:class:`~pynwb.behavior.BehavioralEpochs`,
      :py:class:`~pynwb.behavior.BehavioralEvents`,
      :py:class:`~pynwb.behavior.BehavioralTimeSeries`,
      :py:class:`~pynwb.behavior.CompassDirection`,
      :py:class:`~pynwb.behavior.PupilTracking`,
      :py:class:`~pynwb.behavior.Position`,
      :py:class:`~pynwb.behavior.EyeTracking`.

    * **Extracellular electrophysiology:** :py:class:`~pynwb.ecephys.EventDetection`,
      :py:class:`~pynwb.ecephys.EventWaveform`,
      :py:class:`~pynwb.ecephys.FeatureExtraction`,
      :py:class:`~pynwb.ecephys.FilteredEphys`,
      :py:class:`~pynwb.ecephys.LFP`.

    * **Optical physiology:** :py:class:`~pynwb.ophys.DfOverF`,
      :py:class:`~pynwb.ophys.Fluorescence`,
      :py:class:`~pynwb.ophys.ImageSegmentation`,
      :py:class:`~pynwb.ophys.MotionCorrection`.

    * **Others:** :py:class:`~pynwb.retinotopy.ImagingRetinotopy`,
      :py:class:`~pynwb.base.Images`.

    * **TimeSeries:** Any :ref:`timeseries_overview` is also a subclass of :py:class:`~pynwb.core.NWBDataInterface`
      and can be used anywhere :py:class:`~pynwb.core.NWBDataInterface` is allowed.

.. note::

    In addition to :py:class:`~pynwb.core.NWBContainer`, which functions as a common base type for Group objects,
    :py:class:`~pynwb.core.NWBData` provides a common base for the specification of datasets in the NWB format.

.. _basics_background:

Background: Basic concepts
--------------------------

In the `NWB Format <https://nwb-schema.readthedocs.io>`_, each experimental session is typically
represented by a separate NWB file. NWB files are represented in PyNWB by :py:class:`~pynwb.file.NWBFile`
objects which provide functionality for creating and retrieving:

 * :ref:`timeseries_overview` datasets, i.e., objects for storing time series data
 * :ref:`modules_overview`, i.e., objects for storing and grouping analyses, and
 * experimental metadata and other metadata related to data provenance.

The following sections describe the :py:class:`~pynwb.base.TimeSeries` and :py:class:`~pynwb.base.ProcessingModules`
classes in further detail.

.. _timeseries_overview:

TimeSeries
^^^^^^^^^^

:py:class:`~pynwb.base.TimeSeries` objects store time series data and correspond to the *TimeSeries* specifications
provided by the `NWB Format`_ . Like the NWB specification, :py:class:`~pynwb.base.TimeSeries` Python objects
follow an object-oriented inheritance pattern, i.e., the class :py:class:`~pynwb.base.TimeSeries`
serves as the base class for all other :py:class:`~pynwb.base.TimeSeries` types, such as,
:py:class:`~pynwb.ecephys.ElectricalSeries`, which itself may have further subtypes, e.g.,
:py:class:`~pynwb.ecephys.SpikeEventSeries`.

.. seealso::

    For your reference, NWB defines the following main :py:class:`~pynwb.base.TimeSeries` subtypes:

    * **Extracellular electrophysiology:**
      :py:class:`~pynwb.ecephys.ElectricalSeries`, :py:class:`~pynwb.ecephys.SpikeEventSeries`

    * **Intracellular electrophysiology:**
      :py:class:`~pynwb.icephys.PatchClampSeries` is the base type for all intracellular time series, which
      is further refined into subtypes depending on the type of recording:
      :py:class:`~pynwb.icephys.CurrentClampSeries`,
      :py:class:`~pynwb.icephys.IZeroClampSeries`,
      :py:class:`~pynwb.icephys.CurrentClampStimulusSeries`,
      :py:class:`~pynwb.icephys.VoltageClampSeries`,
      :py:class:`~pynwb.icephys.VoltageClampStimulusSeries`.

    * **Optical physiology and imaging:** :py:class:`~pynwb.image.ImageSeries` is the base type
      for image recordings and is further refined by the
      :py:class:`~pynwb.image.ImageMaskSeries`,
      :py:class:`~pynwb.image.OpticalSeries`, and
      :py:class:`~pynwb.ophys.TwoPhotonSeries` types.
      Other related time series types are:
      :py:class:`~pynwb.image.IndexSeries` and
      :py:class:`~pynwb.ophys.RoiResponseSeries`.

    * **Others** :py:class:`~pynwb.ogen.OptogeneticSeries`,
      :py:class:`~pynwb.behavior.SpatialSeries`,
      :py:class:`~pynwb.misc.DecompositionSeries`,
      :py:class:`~pynwb.misc.AnnotationSeries`,
      :py:class:`~pynwb.misc.AbstractFeatureSeries`, and
      :py:class:`~pynwb.misc.IntervalSeries`.


.. _modules_overview:

Processing Modules
^^^^^^^^^^^^^^^^^^

Processing modules are objects that group together common analyses done during processing of data.
Processing module objects are unique collections of analysis results. To standardize the storage of
common analyses, NWB provides the concept of an :py:class:`~pynwb.core.NWBDataInterface`, where the output of
common analyses are represented as objects that extend the :py:class:`~pynwb.core.NWBDataInterface` class.
In most cases, you will not need to interact with the :py:class:`~pynwb.core.NWBDataInterface` class directly.
More commonly, you will be creating instances of classes that extend this class.


.. seealso::

    For your reference, NWB defines the following main analysis :py:class:`~pynwb.core.NWBDataInterface` subtypes:

    * **Behavior:** :py:class:`~pynwb.behavior.BehavioralEpochs`,
      :py:class:`~pynwb.behavior.BehavioralEvents`,
      :py:class:`~pynwb.behavior.BehavioralTimeSeries`,
      :py:class:`~pynwb.behavior.CompassDirection`,
      :py:class:`~pynwb.behavior.PupilTracking`,
      :py:class:`~pynwb.behavior.Position`,
      :py:class:`~pynwb.behavior.EyeTracking`.

    * **Extracellular electrophysiology:** :py:class:`~pynwb.ecephys.EventDetection`,
      :py:class:`~pynwb.ecephys.EventWaveform`,
      :py:class:`~pynwb.ecephys.FeatureExtraction`,
      :py:class:`~pynwb.ecephys.FilteredEphys`,
      :py:class:`~pynwb.ecephys.LFP`.

    * **Optical physiology:** :py:class:`~pynwb.ophys.DfOverF`,
      :py:class:`~pynwb.ophys.Fluorescence`,
      :py:class:`~pynwb.ophys.ImageSegmentation`,
      :py:class:`~pynwb.ophys.MotionCorrection`.

    * **Others:** :py:class:`~pynwb.retinotopy.ImagingRetinotopy`,
      :py:class:`~pynwb.base.Images`.

    * **TimeSeries:** Any :ref:`timeseries_overview` is also a subclass of :py:class:`~pynwb.core.NWBDataInterface`
      and can be used anywhere :py:class:`~pynwb.core.NWBDataInterface` is allowed.

.. note::

    In addition to :py:class:`~pynwb.core.NWBContainer`, which functions as a common base type for Group objects,
    :py:class:`~pynwb.core.NWBData` provides a common base for the specification of datasets in the NWB format.

The following examples will reference variables that may not be defined within the block they are used in. For
clarity, we define them here:
"""
# sphinx_gallery_thumbnail_path = 'figures/gallery_thumbnails_file.png'
import numpy as np
from pynwb import NWBFile, TimeSeries, NWBHDF5IO
from pynwb.epoch import TimeIntervals
from pynwb.file import Subject
from pynwb.behavior import SpatialSeries, Position
from pynwb.image import RGBAImage, RGBImage, GrayscaleImage
from pynwb.base import Images
from PIL import Image
from datetime import datetime
from dateutil import tz

####################
# .. _basics_nwbfile:
#
# The NWB file
# ------------
#
# An :py:class:`~pynwb.file.NWBFile` represents a single session of an experiment.
# Each :py:class:`~pynwb.file.NWBFile` must have a session description, identifier, and session start time.
# Importantly, the session start time is the reference time for all timestamps in the file.
# For instance, an event with a timestamp of 0 in the file means the event
# occurred exactly at the session start time.
#
# Create an :py:class:`~pynwb.file.NWBFile` object with the required fields
# (``session_description``, ``identifier``, ``session_start_time``) and additional metadata.
#
# .. note::
#     Use keyword arguments when constructing :py:class:`~pynwb.file.NWBFile` objects.
#

session_start_time = datetime(2018, 4, 25, 2, 30, 3, tzinfo=tz.gettz("US/Pacific"))

nwbfile = NWBFile(
    session_description="Mouse exploring an open field",  # required
    identifier="Mouse5_Day3",  # required
    session_start_time=session_start_time,  # required
    session_id="session_1234",  # optional
    experimenter="My Name",  # optional
    lab="My Lab Name",  # optional
    institution="University of My Institution",  # optional
    related_publications="DOI:10.1016/j.neuron.2016.12.011",  # optional
)
print(nwbfile)

####################
# .. _basic_subject:
#
# Subject Information
# ----------------
#
# In the :py:class:`~pynwb.file.Subject` object we can store information about the experimental subject,
# such as ``age``, ``species``, ``genotype``, ``sex``, and a ``description``.
#
# .. only:: html
#
#   .. image:: ../../_static/Subject.svg
#     :width: 150
#     :alt: subject UML diagram
#     :align: center
#
# .. only:: latex
#
#   .. image:: ../../_static/Subject.png
#     :width: 150
#     :alt: subject UML diagram
#     :align: center
#
# The fields in the :py:class:`~pynwb.file.Subject` object are all free-form text (any format will be valid),
# however it is recommended to follow particular conventions to help software tools interpret the data:
#
# * **age**: `ISO 8601 Duration format <https://en.wikipedia.org/wiki/ISO_8601#Durations>`_, e.g., ``"P90D"`` for 90 days old
# * **species**: The formal latin binomial nomenclature, e.g., ``"Mus musculus"``, ``"Homo sapiens"``
# * **sex**: Single letter abbreviation, e.g., ``"F"`` (female), ``"M"`` (male), ``"U"`` (unknown), and ``"O"`` (other)
#
# Add the subject information to the :py:class:`~pynwb.file.NWBFile`
# by setting the ``subject`` field to the new :py:class:`~pynwb.file.Subject` object.

nwbfile.subject = Subject(
    subject_id="001",
    age="P90D",
    description="mouse 5",
    species="Mus musculus",
    sex="M",
)

####################
# .. _basic_timeseries:
#
# Time Series Data
# ----------------
#
# :py:class:`~pynwb.base.TimeSeries` is a common base class for measurements sampled over time,
# and provides fields for ``data`` and ``timestamps`` (regularly or irregularly sampled).
# You will also need to supply the ``name`` and ``unit`` of measurement
# (`SI unit <https://en.wikipedia.org/wiki/International_System_of_Units>`_).
#
# .. image:: ../../_static/TimeSeries.png
#   :width: 200
#   :alt: timeseries UML diagram
#   :align: center
#
# For instance, we can store a :py:class:`~pynwb.base.TimeSeries` data where recording started
# ``0.0`` seconds after ``start_time`` and sampled every second:

data = list(range(100, 200, 10))
time_series_with_rate = TimeSeries(
    name="test_timeseries",
    data=data,
    unit="m",
    starting_time=0.0,
    rate=1.0,
)

####################
# For irregularly sampled recordings, we need to provide the ``timestamps`` for the ``data``:

timestamps = list(range(10))
time_series_with_timestamps = TimeSeries(
    name="test_timeseries",
    data=data,
    unit="m",
    timestamps=timestamps,
)

####################
# :py:class:`~pynwb.base.TimeSeries` objects can be added directly to :py:class:`~pynwb.file.NWBFile` using:
#
# * :py:meth:`~pynwb.file.NWBFile.add_acquisition` to  add *acquisition* data (raw, acquired data that should never change),
# * :py:meth:`~pynwb.file.NWBFile.add_stimulus` to add *stimulus* data, or
# * :py:meth:`~pynwb.file.NWBFile.add_stimulus_template` to store *stimulus templates*.
#

nwbfile.add_acquisition(time_series_with_timestamps)

####################
# We can access the :py:class:`~pynwb.base.TimeSeries` object ``'test_timeseries'``
# in :py:class:`~pynwb.file.NWBFile` from ``acquisition``:

nwbfile.acquisition["test_timeseries"]

####################
# or using the :py:meth:`~pynwb.file.NWBFile.get_acquisition` method:
nwbfile.get_acquisition("test_timeseries")


####################
# .. _basic_spatialseries:
#
# Spatial Series and Position
# ----------------
#
# :py:class:`~pynwb.behavior.SpatialSeries` is a subclass of :py:class:`~pynwb.base.TimeSeries`
# that represents the spatial position of an animal over time.
#
# .. only:: html
#
#   .. image:: ../../_static/SpatialSeries.svg
#     :width: 200
#     :alt: spatialseries UML diagram
#     :align: center
#
# .. only:: latex
#
#   .. image:: ../../_static/SpatialSeries.png
#     :width: 200
#     :alt: spatialseries UML diagram
#     :align: center
#
# Create a :py:class:`~pynwb.behavior.SpatialSeries` object named ``"SpatialSeries"`` with some fake data.

# create fake data with shape (50, 2)
# the first dimension should always represent time
position_data = np.array([np.linspace(0, 10, 50), np.linspace(0, 8, 50)]).T
position_timestamps = np.linspace(0, 50) / 200

spatial_series_obj = SpatialSeries(
    name="SpatialSeries",
    description="(x,y) position in open field",
    data=position_data,
    timestamps=position_timestamps,
    reference_frame="(0,0) is bottom left corner",
)
print(spatial_series_obj)

####################
# To help data analysis and visualization tools know that this :py:class:`~pynwb.behavior.SpatialSeries` object
# represents the position of the subject, store the :py:class:`~pynwb.behavior.SpatialSeries` object inside
# of a :py:class:`~pynwb.behavior.Position` object, which can hold one or more :py:class:`~pynwb.behavior.SpatialSeries` objects.
#
# .. only:: html
#
#   .. image:: ../../_static/Position.svg
#     :width: 450
#     :alt: position UML diagram
#     :align: center
#
# .. only:: latex
#
#   .. image:: ../../_static/Position.png
#     :width: 450
#     :alt: position UML diagram
#     :align: center
#
# Create a :py:class:`~pynwb.behavior.Position` object named ``"Position"`` [#]_.

# name is set to "Position" by default
position_obj = Position(spatial_series=spatial_series_obj)

####################
# Behavior Processing Module
# ----------------
#
# :py:class:`~pynwb.base.ProcessingModule` is a container for data interfaces that are related to a particular
# processing workflow. NWB differentiates between raw, acquired data (*acquisition*), which should never change,
# and processed data (*processing*), which are the results of preprocessing algorithms and could change.
# Processing modules can be thought of as folders within the file for storing the related processed data.
#
# .. tip:: Use the NWB schema module names as processing module names where appropriate.
#    These are: ``"behavior"``, ``"ecephys"``, ``"icephys"``, ``"ophys"``, ``"ogen"``, ``"retinotopy"``, and ``"misc"``.
#
# Let's assume that the subject's position was computed from a video tracking algorithm,
# so it would be classified as processed data.
#
# Create a processing module called ``"behavior"`` for storing behavioral data in the :py:class:`~pynwb.file.NWBFile`
# and add the :py:class:`~pynwb.behavior.Position` object to the processing module using the
# :py:meth:`~pynwb.file.NWBFile.create_processing_module` method:


behavior_module = nwbfile.create_processing_module(
    name="behavior", description="processed behavioral data"
)
behavior_module.add(position_obj)

####################
#
# .. only:: html
#
#   .. image:: ../../_static/Behavior.svg
#     :width: 600
#     :alt: behavior UML diagram
#     :align: center
#
# .. only:: latex
#
#   .. image:: ../../_static/Behavior.png
#     :width: 600
#     :alt: behavior UML diagram
#     :align: center
#
# Once the behavior processing module is added to the :py:class:`~pynwb.file.NWBFile`,
# you can access it with:

print(nwbfile.processing["behavior"])

####################
# .. _basic_writing:
#
# Writing an NWB file
# -------------------
#
# NWB I/O is carried out using the :py:class:`~pynwb.NWBHDF5IO` class [#]_. This class is responsible
# for mapping an :py:class:`~pynwb.file.NWBFile` object into HDF5 according to the NWB schema.
#
# To write an :py:class:`~pynwb.file.NWBFile`, use the :py:meth:`~hdmf.backends.io.HDMFIO.write` method.

io = NWBHDF5IO("basics_tutorial.nwb", mode="w")
io.write(nwbfile)
io.close()

####################
# You can also use :py:meth:`~pynwb.NWBHDF5IO` as a context manager:

with NWBHDF5IO("basics_tutorial.nwb", "w") as io:
    io.write(nwbfile)

####################
# .. _basic_reading:
#
# Reading an NWB file
# -------------------
#
# As with writing, reading is also carried out using the :py:class:`~pynwb.NWBHDF5IO` class.
# To read the NWB file we just wrote, use another :py:class:`~pynwb.NWBHDF5IO` object,
# and use the :py:meth:`~pynwb.NWBHDF5IO.read` method to retrieve an
# :py:class:`~pynwb.file.NWBFile` object.
#
# Data arrays are read passively from the file.
# Accessing the ``data`` attribute of the :py:class:`~pynwb.base.TimeSeries` object
# does not read the data values, but presents an HDF5 object that can be indexed to read data.
# You can use the ``[:]`` operator to read the entire data array into memory.

with NWBHDF5IO("basics_tutorial.nwb", "r") as io:
    read_nwbfile = io.read()
    print(read_nwbfile.acquisition["test_timeseries"])
    print(read_nwbfile.acquisition["test_timeseries"].data[:])

####################
# It is often preferable to read only a portion of the data.
# To do this, index or slice into the ``data`` attribute just like if you were
# indexing or slicing a numpy array.

with NWBHDF5IO("basics_tutorial.nwb", "r") as io:
    read_nwbfile = io.read()
    print(read_nwbfile.acquisition["test_timeseries"])
    print(read_nwbfile.acquisition["test_timeseries"].data[:2])

####################
# .. note::
#     If you use :py:class:`~pynwb.NWBHDF5IO` as a context manager during read,
#     be aware that the :py:class:`~pynwb.NWBHDF5IO` gets closed and when the
#     context completes and the data will not be available outside of the
#     context manager [#]_.

####################
# Accessing data
# ^^^^^^^^^^^^^^^
#
# We can also access the :py:class:`~pynwb.behavior.SpatialSeries` data by referencing the names
# of the objects in the hierarchy that contain it. We can access a processing module by indexing
# ``"nwbfile.processing"`` with the name of the processing module, ``"behavior"``.
#
# Then, we can access the :py:class:`~pynwb.behavior.Position` object inside of the ``"behavior"``
# processing module by indexing it with the name of the :py:class:`~pynwb.behavior.Position` object,
# ``"Position"``.
#
# Finally, we can access the :py:class:`~pynwb.behavior.SpatialSeries` object inside of the
# :py:class:`~pynwb.behavior.Position` object by indexing it with the name of the
# :py:class:`~pynwb.behavior.SpatialSeries` object, ``"SpatialSeries"``.

with NWBHDF5IO("basics_tutorial.nwb", "r") as io:
    read_nwbfile = io.read()
    print(read_nwbfile.processing["behavior"])
    print(read_nwbfile.processing["behavior"]["Position"])
    print(read_nwbfile.processing["behavior"]["Position"]["SpatialSeries"])

####################

# .. _reuse_timestamps:
#
# Reusing timestamps
# ------------------
#
# When working with multi-modal data, it can be convenient and efficient to store timestamps once and associate multiple
# data with the single timestamps instance. PyNWB enables this by letting you reuse timestamps across
# :py:class:`~pynwb.base.TimeSeries` objects. To reuse a :py:class:`~pynwb.base.TimeSeries` timestamps in a new
# :py:class:`~pynwb.base.TimeSeries`, pass the existing :py:class:`~pynwb.base.TimeSeries` as the new
# :py:class:`~pynwb.base.TimeSeries` timestamps:

data = list(range(101, 201, 10))
reuse_ts = TimeSeries(
    name="reusing_timeseries",
    data=data,
    unit="SIunit",
    timestamps=time_series_with_timestamps,
)


####################
# Time Intervals
# --------------
#
# .. _basic_trials:
#
# Trials
# ^^^^^^
#
# Trials are stored in :py:class:`pynwb.epoch.TimeIntervals` object which is
# a subclass of :py:class:`pynwb.core.DynamicTable`.
# :py:class:`pynwb.core.DynamicTable` objects are used to store tabular metadata
# throughout NWB, including trials, electrodes and sorted units. They offer
# flexibility for tabular data by allowing required columns, optional columns,
# and custom columns which are not defined in the standard.
#
# .. only:: html
#
#   .. image:: ../../_static/Trials.svg
#     :width: 300
#     :alt: trials UML diagram
#     :align: center
#
# .. only:: latex
#
#   .. image:: ../../_static/Trials.png
#     :width: 300
#     :alt: trials UML diagram
#     :align: center
#
# The ``trials`` :py:class:`pynwb.core.DynamicTable` can be thought of
# as a table with this structure:
#
# .. image:: ../../_static/trials_example.png
#   :width: 400
#   :alt: trials table example
#   :align: center
#
# Trials can be added to the :py:class:`~pynwb.file.NWBFile` using the
# methods :py:meth:`~pynwb.file.NWBFile.add_trial_column` and :py:meth:`~pynwb.file.NWBFile.add_trial`
# We can add custom, user-defined columns to the trials table to hold data
# and metadata specific to this experiment or session.
# By default, :py:class:`~pynwb.file.NWBFile` only requires the ``start_time``
# and ``end_time`` of the trial. Additional columns can be added using
# the :py:meth:`~pynwb.file.NWBFile.add_trial_column` method.
#
# Continue adding to our :py:class:`~pynwb.file.NWBFile` by creating a new
# column for the trials table named ``'correct'``, which will be a boolean array.
# Once all columns have been added, trial data can be populated using
# :py:meth:`~pynwb.file.NWBFile.add_trial`.

nwbfile.add_trial_column(
    name="correct",
    description="whether the trial was correct",
)
nwbfile.add_trial(start_time=1.0, stop_time=5.0, correct=True)
nwbfile.add_trial(start_time=6.0, stop_time=10.0, correct=False)

####################
# Tabular data such as trials can be converted to a :py:class:`~pandas.DataFrame`.

print(nwbfile.trials.to_dataframe())

####################
# .. _basic_epochs:
#
# Epochs
# ^^^^^^
#
# Epochs can be added to an NWB file using the method :py:meth:`~pynwb.file.NWBFile.add_epoch`.
# The first and second arguments are the start time and stop times, respectively.
# The third argument is one or more tags for labeling the epoch, and the fourth argument is a
# list of all the :py:class:`~pynwb.base.TimeSeries` that the epoch applies
# to.

nwbfile.add_epoch(
    start_time=2.0,
    stop_time=4.0,
    tags=["first", "example"],
    timeseries=[time_series_with_timestamps],
)

nwbfile.add_epoch(
    start_time=6.0,
    stop_time=8.0,
    tags=["second", "example"],
    timeseries=[time_series_with_timestamps],
)

####################
# Other time intervals
# ^^^^^^^^^^^^^^^^^^^^
# Both ``epochs`` and ``trials`` are of of data type :py:class:`~pynwb.epoch.TimeIntervals`, which is a type of
# ``DynamicTable`` for storing information about time intervals. ``"epochs"`` and ``"trials"``
# are the two default names for :py:class:`~pynwb.base.TimeIntervals` objects, but you can also add your own

sleep_stages = TimeIntervals(
    name="sleep_stages",
    description="intervals for each sleep stage as determined by EEG",
)

sleep_stages.add_column(name="stage", description="stage of sleep")
sleep_stages.add_column(name="confidence", description="confidence in stage (0-1)")

sleep_stages.add_row(start_time=0.3, stop_time=0.5, stage=1, confidence=0.5)
sleep_stages.add_row(start_time=0.7, stop_time=0.9, stage=2, confidence=0.99)
sleep_stages.add_row(start_time=1.3, stop_time=3.0, stage=3, confidence=0.7)

nwbfile.add_time_intervals(sleep_stages)

####################
# Images
# ------
#
# You can store static images within the NWB file as well. These can be images of the subject, the environment, stimuli,
# or really anything.
#
# .. note::
#          All basic image types :py:class:`~pynwb.image.RGBAImage`, :py:class:`~pynwb.image.RGBImage`, and
#          :py:class:`~pynwb.image.GrayscaleImage` provide the optional: 1) ``description`` parameter to include a
#          text description about the image and 2) ``resolution`` parameter to specify the *pixels / cm* resolution
#          of the image.

img = Image.open("docs/source/logo.png")  # an example image

# you can store an RGBA image
rgba_logo = RGBAImage(name="RGBA_logo", data=np.array(img))

# or RGB
rgb_logo = RGBImage(name="RGB_logo", data=np.array(img.convert("RGB")))

# or Grayscale. Here with the optional description and resolution specified.
gs_logo = GrayscaleImage(
    name="Grayscale_logo",
    data=np.array(img.convert("L")),
    description="Grayscale version of the NWB logo",
    resolution=35.433071,
)

# Images is a container that accepts any of these image types
images = Images(name="logo_images", images=[rgb_logo, rgba_logo, gs_logo])

# Finally, do not forget to add the images object to the nwb file.
nwbfile.processing["behavior"].add(images)

####################
# Now we overwrite the file with all of the data

with NWBHDF5IO("basics_tutorial.nwb", "w") as io:
    io.write(nwbfile)

####################
# .. _basic_appending:
#
# Appending to an NWB file
# ------------------------
#
# Using functionality discussed above, NWB allows appending to files. To append to a file, you must read the file, add
# new components, and then write the file. Reading and writing is carried out using :py:class:`~pynwb.NWBHDF5IO`.
# When reading the NWBFile, you must specify that you intend to modify it by setting the *mode* argument in the
# :py:class:`~pynwb.NWBHDF5IO` constructor to ``'a'``. After you have read the file, you can add [#]_ new data to it
# using the standard write/add functionality demonstrated above.
#
# Let's see how this works by adding another :py:class:`~pynwb.base.TimeSeries` to the BehavioralTimeSeries interface
# we created above.
#
# First, read the file and get the interface object.

io = NWBHDF5IO("basics_tutorial.nwb", mode="a")
nwbfile = io.read()
position = nwbfile.processing["behavior"].data_interfaces["Position"]

####################
# Next, add a new :py:class:`~pynwb.behavior.SpatialSeries`.

data = list(range(300, 400, 10))
timestamps = list(range(10))

new_spatial_series = SpatialSeries(
    name="SpatialSeriesAppended",
    data=data,
    timestamps=timestamps,
    reference_frame="starting_gate",
)
position.add_spatial_series(new_spatial_series)
print(position)

####################
# Finally, write the changes back to the file and close it.

io.write(nwbfile)
io.close()

####################
# .. [#] Some data interface objects have a default name. This default name is the type of the data interface. For
#    example, the default name for :py:class:`~pynwb.ophys.ImageSegmentation` is "ImageSegmentation" and the default
#    name for :py:class:`~pynwb.ecephys.EventWaveform` is "EventWaveform".
#
# .. [#] HDF5 is currently the only backend supported by NWB.
#
# .. [#] Neurodata sets can be *very* large, so individual components of the dataset are only loaded into memory when
#    you request them. This functionality is only possible if an open file handle is kept around until users want to
#    load data.
#
# .. [#] NWB only supports *adding* to files. Removal and modifying of existing data is not allowed.

####################
# .. _hck04: https://github.com/NeurodataWithoutBorders/nwb_hackathons/tree/master/HCK04_2018_Seattle
