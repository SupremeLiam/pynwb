# PyNWB Changelog

## PyNWB 2.0.1 (March 16, 2022)

### Bug fixes:
- Add `environment-ros3.yml` to `MANIFEST.in` for inclusion in source distributions. @rly (#1398)
- Fix bad error check in ``IntracellularRecordingsTable.add_recording`` when adding ``IZeroClampSeries``. @oruebel (#1410)
- Skip ros3 tests if internet access or the ros3 driver are not available. @oruebel (#1414)
- Fix CI issues. @rly (#1427)

### Documentation and tutorial enhancements:
- Enhanced ordering of sphinx gallery tutorials to use alphabetic ordering based on tutorial headings. @oruebel (#1399)
- Updated the general tutorial to add documentation about the ``Images`` type. @bendichter (#1353)
- Updated the main index of the documentation to make the documentation easier to navigate. @oruebel (#1402)
- Merged the "NWB File" overview section with the "NWB File Basics" tutorial. @oruebel (#1402)
- Updated and created separated installation instructions for users and developers . @oruebel (#1402)
- Updated the Extracellular electrophysiology tutorial. @bendichter, @weiglszonja (#1391)
- Extended the general tutorial with more data types (e.g., ``Subject``, ``SpatialSeries``, ``Position``).
  @weiglszonja (#1403)
- Improved constructor docstrings for Image types. @weiglszonja (#1418)
- Added documentation for exporting NWB files. @rly (#1417)
- Improved documentation formatting. @bendichter (#1438)
- Minor text fixes. @bendichter (#1437, #1400)

### Minor improvements:
- Added checks for data orientation in ``TimeSeries``, ``ElectricalSeries``, and ``RoiResponseSeries``.
  @bendichter (#1426)
- Enhanced issue template forms on GitHub. @CodyCBakerPHD (#1434)


## PyNWB 2.0.0 (August 13, 2021)

### Breaking changes:
- ``SweepTable`` has been deprecated in favor of the new icephys metadata tables. Use of ``SweepTable``
  is still possible but no longer recommended. @oruebel  (#1349)
- ``TimeSeries.__init__`` now requires the ``data`` argument because the 'data' dataset is required by the schema.
  If a ``TimeSeries`` is read without a value for ``data``, it will be set to a default value. For most
  ``TimeSeries``, this is a 1-dimensional empty array with dtype uint8. For ``ImageSeries`` and
  ``DecompositionSeries``, this is a 3-dimensional empty array with dtype uint8. @rly (#1274)
- ``TimeSeries.__init__`` now requires the ``unit`` argument because the 'unit' attribute is required by the schema.
  If a ``TimeSeries`` is read without a value for ``unit``, it will be set to a default value. For most
  ``TimeSeries``, this is "unknown". For ``IndexSeries``, this is "N/A" according to the NWB 2.4.0 schema. @rly (#1274)

### New features:
- Added new intracellular electrophysiology hierarchical table structure from ndx-icephys-meta to NWB core.
  This includes the new types ``TimeSeriesReferenceVectorData``, ``IntracellularRecordingsTable``,
  ``SimultaneousRecordingsTable``, ``SequentialRecordingsTable``, ``RepetitionsTable`` and
  ``ExperimentalConditionsTable`` as well as corresponding updates to ``NWBFile`` to support interaction
   with the new tables. @oruebel  (#1349)
- Added support for NWB 2.4.0. See [Release Notes](https://nwb-schema.readthedocs.io/en/latest/format_release_notes.html)
  for more details. @oruebel, @rly (#1349)
- Dropped Python 3.6 support, added Python 3.9 support. @rly (#1377)
- Updated requirements to allow compatibility with HDMF 3 and h5py 3. @rly (#1377)
  - When using HDMF 3 and h5py 3, users can now stream NWB files from an S3 bucket.

### Tutorial enhancements:
- Added new tutorial for intracellular electrophysiology to describe the use of the new metadata tables
  and declared the previous tutoral using ``SweepTable`` as deprecated.  @oruebel (#1349)
- Added new tutorial for querying intracellular electrophysiology metadata
  (``docs/gallery/domain/plot_icephys_pandas.py``). @oruebel (#1349, #1383)
- Added thumbnails for tutorials to improve presentation of online docs.  @oruebel (#1349)
- Used `sphinx.ext.extlinks` extension in docs to simplify linking to common targets. @oruebel (#1349)
- Created new section for advanced I/O tutorials and moved parallel I/O tutorial to its own file. @oruebel (#1349)
- Overhauled documentation on extensions. @bendichter, @rly, @oruebel (#1350)
- Updated the optical physiology / Calcium imaging tutorial. @bendichter, @weiglszonja (#1375)
- Added a tutorial on streaming using the ROS3 driver. @rly (#1393)

### Minor new features:
- Added RRID for citing PyNWB to the docs. @oruebel (#1372)
- Updated CI and tests to handle deprecations in libraries. @rly (#1377)
- Added test utilities for icephys (``pynwb.testing.icephys_testutils``) to ease creation of test data
  for tests and tutorials. @oruebel (#1349, #1383)
- Added on-push and nightly tests of streaming using the ROS3 driver. @rly (#1393)
  - These tests make use of a new dandiset for testing the API: https://gui.dandiarchive.org/#/dandiset/000126
- Improve documentation and test for ``CorrectedImageStack``, ``MotionCorrection``. @rly, @bendichter (#1306, #1374)

### Bug fixes:
- Updated behavior of ``make clean`` command for docs to ensure tutorial files are cleaned up.  @oruebel (#1349)
- Enforced electrode ID uniqueness during insertion into table. @CodyCBakerPhD (#1344)
- Fixed integration tests with invalid test data that will be caught by future hdmf validator version.
  @dsleiter, @rly (#1366, #1376)
- Fixed build warnings in docs. @oruebel (#1380)
- Fix intersphinx links in docs for numpy. @oruebel (#1386)
- Previously, the ``data`` argument was required in ``OpticalSeries.__init__`` even though ``external_file`` could
  be provided in place of ``data``. ``OpticalSeries.__init__`` now makes ``data`` optional. However, this has the
  side effect of moving the position of ``data`` to later in the argument list, which may break code that relies
  on positional arguments for ``OpticalSeries.__init__``. @rly (#1274)
- Fixed `setup.py` not being able to import `versioneer` when installing in an embedded Python environment. @ikhramts
  (#1395)
- Removed broken option to validate against a given namespace file and updated associated documentation. @rly (#1397)

## PyNWB 1.5.1 (May 24, 2021)

### Bug fixes:
- Raise minimum version of pandas from 0.23 to 1.0.5 to be compatible with numpy 1.20, and raise minimum version of
  HDMF to use the corresponding change in HDMF. @rly (#1363)
- Update documentation and update structure of requirements files. @rly (#1363)

## PyNWB 1.5.0 (May 17, 2021)

### New features:
- `NWBFile.add_scratch(...)` and `ScratchData.__init__(...)` now accept scalar data in addition to the currently
  accepted types. @rly (#1309)
- Support `pathlib.Path` paths when opening files with `NWBHDF5IO`. @dsleiter (#1314)
- Use HDMF 2.5.1. See the [HDMF release notes](https://github.com/hdmf-dev/hdmf/releases/tag/2.5.1) for details.
- Support `driver='ros3'` in `NWBHDF5IO` for streaming NWB files directly from s3. @bendichter (#1331)
- Update documentation, CI GitHub processes. @oruebel @yarikoptic, @bendichter, @TomDonoghue, @rly
  (#1311, #1336, #1351, #1352, #1345, #1340, #1327)
- Set default `neurodata_type_inc` for `NWBGroupSpec`, `NWBDatasetSpec`. @rly (#1295)
- Block usage of h5py 3+ for now. h5py>=2.9, <3 is supported. (#1355)
- Fix incompatibility issue with downstream github-release tool used to deploy releases to GitHub. @rly (#1245)
- Fix issue with Sphinx gallery. @rly
- Add citation information to documentation and support for duecredit tool. @rly
- Remove use of ColoredTestRunner for more readable verbose test output. @rly
- Add support for nwb-schema 2.3.0. @rly (#1245, #1330)
  - Add optional `waveforms` column to the `Units` table.
  - Add optional `strain` field to `Subject`.
  - Add to `DecompositionSeries` an optional `DynamicTableRegion` called `source_channels`.
  - Add to `ImageSeries` an optional link to `Device`.
  - Add optional `continuity` field to `TimeSeries`.
  - Add optional `filtering` attribute to `ElectricalSeries`.
  - Clarify documentation for electrode impedance and filtering.
  - Set the `stimulus_description` for `IZeroCurrentClamp` to have the fixed value "N/A".
  - See https://nwb-schema.readthedocs.io/en/latest/format_release_notes.html for full schema release notes.
- Add support for HDMF 2.5.5 and upgrade HDMF requirement from 2.1.0 to 2.5.5. @rly @ajtritt
  (#1325, #1355, #1360, #1245, #1287). This includes several relevant features and bug fixes, including:
  - Fix issue where dependencies of included types were not being loaded in namespaces / extensions.
  - Add `HDF5IO.get_namespaces(path=path, file=file)` method which returns a dict of namespace name mapped to the
    namespace version (the largest one if there are multiple) for each namespace cached in the given HDF5 file.
  - Add methods for automatic creation of `MultiContainerInterface` classes.
  - Add ability to specify a custom class for new columns to a `DynamicTable` that are not `VectorData`,
    `DynamicTableRegion`, or `VocabData` using `DynamicTable.__columns__` or `DynamicTable.add_column(...)`.
  - Add support for creating and specifying multi-index columns in a `DynamicTable` using `add_column(...)`.
  - Add capability to add a row to a column after IO.
  - Add method `AbstractContainer.get_fields_conf`.
  - Add functionality for storing external resource references.
  - Add method `hdmf.utils.get_docval_macro` to get a tuple of the current values for a docval_macro, e.g., 'array_data'
    and 'scalar_data'.
  - `DynamicTable` can be automatically generated using `get_class`. Now the HDMF API can read files with extensions
    that contain a DynamicTable without needing to import the extension first.
  - Add `EnumData` type for storing data that comes from a fixed set of values.
  - Add `AlignedDynamicTable` type which defines a DynamicTable that supports storing a collection of subtables.
  - Allow `np.bool_` as a valid `bool` dtype when validating.
  - See https://github.com/hdmf-dev/hdmf/releases for full HDMF release notes.

## PyNWB 1.4.0 (August 12, 2020)

Users can now add/remove containers from a written NWB file and export the modified NWBFile to a new file path.
@rly (#1280)
- See https://pynwb.readthedocs.io/en/stable/tutorials/general/add-remove-containers.html for examples and more
  information.

### Compatibility warnings:
- PyNWB no longer works with HDMF version < 2.1.0. If you have pinned HDMF version < 2 in your package but allow PyNWB
version 1.4.0, please beware that `pip` may install PyNWB version 1.4.0 with an incompatible version of HDMF
(version < 2).
- Use of HDMF 2.1.0 fixes `__getitem__`-based access of `MultiContainerInterface` types, e.g,,
`fluorescence['roi_response_series_name']`, where previously if the `MultiContainerInterface` contained only one item,
then any key could be used within the square brackets to access the contained `Container`, even if the key did not
match the name of the contained `Container`. This update patches this bug such that the key used within the square
brackets *must* match the name of the contained `Container` or else an error will be raised.

### Internal improvements:
- Update requirements to use HDMF 2.1.0. @rly (#1256)
- Start FAQ section in documentation. @rly (#1249)
- Improve deprecation warnings. @rly (#1261)
- Update CI to test Python 3.8, update requirements. @rly (#1267, #1275)
- Make use of `MultiContainerInterface` and `LabelledDict` that have been moved to HDMF. @bendichter @rly (#1260)

### Bug fixes:
- For `ImageSeries`, add check if `external_file` is provided without `starting_frame` in `__init__`. @rly (#1264)
- Improve docstrings for `TimeSeries.data` and for the electrode table. @rly (#1271, #1272)
- Fix Azure Pipelines configuration. @rly (#1281)

## PyNWB 1.3.3 (June 26, 2020)

### Internal improvements:
- Update requirements to use HDMF 1.6.4. @rly (#1256)

### Bug fixes:
- Fix writing optional args to electrodes table. @rly (#1246)
- Fix missing method UnitsMap.get_nwb_file. @rly (#1227)

## PyNWB 1.3.2 (June 1, 2020)

### Bug fixes:
- Add support for nwb-schema 2.2.5. @rly (#1243)
  - This schema version fixes incorrect dims and shape for `ImagingPlane.origin_coords` and `ImagingPlane.grid_spacing`,
   and fixes incorrect dims for `TwoPhotonSeries.field_of_view`.

## PyNWB 1.3.1 (May 28, 2020)

### Bug fixes:
- Fix bugged `Device` constructor. @rly (#1209)
- Fix link to code of conduct page in docs. @rly (#1229)
- Fix docs for `get_type_map`. @oruebel (#1233)
- Pass file object to parent when loading namespaces. @NileGraddis (#1242)

### Internal improvements:
- Update CI to use supported MacOS version. @rly (#1211)
- Clean up tests to remove conversion warnings and use keyword args. @rly (#1202)
- Fix flake8 errors. @rly (#1235)
- Add changelog. @rly (#1215)
- Update release process with notes about coordinating with nwb-schema. @rly (#1214)
- Inform which unit value is actually overwritten. @yarikoptic (#1219)
- Do not print out logging.DEBUG statements to stdout for test.py. @rly (#1240)
- Add support for nwb-schema 2.2.4. @rly (#1213)
  - Make `ImagingPlane.imaging_rate` optional. This moves the `imaging_rate` argument down the list of constructor arguments for `ImagingPlane.__init__`. This will break existing code that calls the constructor of `ImagingPlane` with at least 6 positional arguments, such that one positional argument matches `imaging_rate`.

## PyNWB 1.3.0 (Mar. 4, 2020)

### New features:
- Add support for nwb-schema 2.2.2. @rly (#1146)
  - This is a large change. See the PR and [schema release notes](http://nwb-schema.readthedocs.io/en/latest/format_release_notes.html#march-2-2020) for more information.
- Validate against most specific namespace. @t-b, @rly (#1094)
- Replace 'ic_electrode' with 'icephys_electrode' in `NWBFile`. @oruebel (#1200)
- Integrate minor enhancements and bug fixes introduced in HDMF 1.6.0 and 1.6.1, including improved handling of namespaces that lack a version key,

### Internal improvements:
- Add nightly testing of validation CLI. @t-b, @rly (#1164, #1195, #1197)
- Treat ipython notebooks as binary in git. @t-b (#1168)
- Use proper file removal in tests. @t-b (#1165)
- Use hdmf-docutils instead of nwb-docutils for documentation. @jcfr (#1176)
- Run minimum requirements testing n Python 3.6. @rly (#1194)

### Bug fixes:
- Fix API documentation. @bendichter (#1159)
- Fix unit testing output. @rly (#1158)
- Fix copying files with Subject. @rly (#1171)
- Add "unit" attribute back as an optional attribute in icephys classes. @rly (#1188)
- Fix reported development status in `setup.py`. @rly (#1201)

## PyNWB 1.2.1 (Jan. 22, 2020)

### Bug fixes:
- Fix ReadTheDocs build. @rly (#1155)
- Update manifest to fix conda build. @rly (#1156)

## PyNWB 1.2.0 (Jan. 21, 2020)

### Minor enhancements:
- Add new logo to docs. @rly (#1096)
- Add warning when referencing electrode table before it exists. @ajtritt (#1098)
- Refactor internal calls to docval. @rly (#1104)
- Enhance icephys example and documentation. @t-b (#1081)
- Add multi index and time bounds to get_unit_spikes. @bendichter (#1001)
- Improve ophys docstrings. @bendichter (#1126)
- Improve icephys docstrings for gain. @bendichter (#1129)
- Update legal information. @rly (#1131)
- Add support for device description and manufacturer. @rly (#1135)
- Update dependencies and remove explicit six, unittest2 dependency. @rly (#1136, #1138, #1142, #1137, #1154)
- Add object ID tutorial. @rly (#1140)
- Update CI. @rly (#1141)
- Catch critical warnings and throw errors in unit tests. @rly (#1112)
- Create and use testing module, remove builder tests, clean up test code. @rly (#1117)
- Add and test minimum requirements for PyNWB. @rly (#1148)
- Improve docs for get_class. @bendichter (#1149)

### Bug fixes:
- Fix versioneer reporting version. @rly (#1100)
- Fix `DynamicTable` import after move to hdmf.common. @bendichter (#1103)
- Fix handling of unmapped attributes. @rly (#1105)
- Update tests and documentation to reflect new selection behavior of `DynamicTable`. @oruebel (#1106)
- Fix reference images not being mapped in PlaneSegmentation. @rly (#1109)
- Fix legacy import of `ObjectMapper`. @rly (#1124)
- Fix extensions documentation typo: 'str' -> 'text'. @bendichter (#1132)
- Revert "PatchClampSeries: Force sweep_number to uint64". @t-b (#1123)
- Fix sphinx code to use latest sphinx. @rly (#1139)

## PyNWB 1.1.2 (Oct. 15, 2019)

### Minor features:
- Use latest HDMF 1.3.3. #1093 (@rly)
- Expose HDMF export_spec utility function for use by extensions. #1092 (@rly)

### Bug fixes:
- Fix bug in writing SpikeEventSeries data or timestamps datasets with a DataChunkIterator. #1089 (@bendichter)

## PyNWB 1.1.1 (Oct. 7, 2019)

PyNWB 1.1.0 does not work with HDMF>=1.3. This release will work with HDMF>=1.3.2.

### Minor improvements:
- Support newly added channel-specific conversion factor for ElectricalSeries #1072 (@bendichter)
- Move generic types out of PyNWB into hdmf-common. #1061 (@ajtritt)
- Update documentation to reflect the above changes. #1078 (@rly)
- Add new case to the iterative write tutorial. #1029 (@oruebel)
- Improve CI. #1079 (@rly)
- Pin the current latest version of HDMF to requirements for setup.py. #1083 (@rly)

## PyNWB 1.1.0 (Sep. 17, 2019)

### New features:
- Add object ID to all neurodata types #991 (@ajtritt, @rly)
- Add NWBFile shallow copy method #994 (@ajtritt, @rly)
- Drop official Python 2.7 support #1028 (@rly)
- Add scratch space #1027 #1038 (@ajtritt, @rly)
- Support multiple experimenters #988 #1035 (@ajtritt, @rly)
- Support multiple related publications #1047 (@rly)
- Update schema to 2.1.0 (see release notes in https://nwb-schema.readthedocs.io/en/latest/format_release_notes.html) (@rly, @bendichter, @ajtritt, @oruebel, @t-b)

### Minor enhancements:
- Add iterative write check for TimeSeries timestamps #1012 (@bendichter, @oruebel)
- Add functions to convert between pixel mask and image mask for ophys data #766 (@mamelara)
- Add cortical surface extension example #1040 (@bendichter)
- Match API with schema defaults #1033 (@rly)
- Core schema is now a git submodule #1045 (@ajtritt)
- Implement better support for floating point data for Python 3.5 on Windows #1043 (@rly)
- Enhance iterative write tutorial #1029 (@oruebel)
- Allow empty data in DynamicTable with non-empty VectorIndex #887 (@ajtritt)
- Allow OpticalSeries constructor argument 'field_of_view' to be H5Dataset #1063 (@bendichter)
- Clarify documentation for deprecated ImageSeries constructor arg 'bits_per_pixel' #1065 (@rly)
- Adjust code to explicitly map properties after changes made in HDMF 1.2 #1048 #1069 (@rly)
- Improvements to CI, documentation, and GitHub repo structure #1055 (@rly)

## PyNWB 1.0.3 (Jul. 18, 2019)

### New/modified functionality:
- Add MPI functionality to NWBHDF5IO (@bendichter)
- Add option to exclude columns from DynamicTable.to_dataframe() (@NileGraddis)
- Remove ability to add DecompositionSeries to LFP (@bendichter)
- Remove num_samples from TimeSeries (@NileGraddis)
- Automatically detect ragged arrays in from_dataframe (@bendichter)
- Cache the spec by default on write (@rly)
- Improve printing of NWB objects (@rly)
- Change ProcessingModule.add_data_interface() to .add(), ProcessingModule.get_data_interface() to .get(), NWBFile.modules to NWBFile.processing (@bendichter)
- Remove unused SpecFile type (@oruebel)
- Add ability to validate files against the cached spec (@t-b)
- Make CurrentClampSeries/VoltageClampSeries parameters optional (@t-b)
- Update documentation (@t-b, @rly)
- Update copyright/license
- Improve tests and CI
- Update requirements
- See also HDMF changes https://github.com/hdmf-dev/hdmf/releases/tag/1.0.4

### Bug fixes:
- Fix dynamictableregion iteration failure after roundtrip (@NileGraddis)
- Fix from_dataframe for children of DynamicTable (@bendichter)
- Fix for modular (cross-file) storage of timeseries timestamps (@NileGraddis)
- Fix bug on loading lists of strings from hdmf 1.0.4 (@rly)
- Fix IO for intervals (@bendichter)
- Fix round trip for Subject.date_of_birth (@bendichter)

### Schema changes:
- DecompositionSeries "source_timeseries" link is no longer required (@bendichter)
- Reorder keys (@rly)
- Remove NWBFile "specifications" group (@oruebel)
- CorrectedImageStack and ImagingRetinotopy inherits from NWBDataInterface instead of NWBContainer (@rly)
- Fix typo in unit of resistance_comp_prediction/correction (@t-b)
- Add option for third dimension for Units "waveforms" dataset to represent different electrodes (@bendichter)
- Update NWBFile.nwb_version to 2.0.2

## PyNWB 1.0.2 (Apr. 19, 2019)
