
archive_tool is a set of common python functions to work with the Kodi archive virtual file system (vfs) binary addons such as [vfs.libarchive](https://github.com/xbmc/vfs.libarchive) and [vfs.rar](https://github.com/xbmc/vfs.rar)

Simplest usage example:
```
import archive_tool

my_archive = archive_tool.archive_tool(archive_file = 'myfile.zip',directory_out = '/my/output_directory/') #Current archive object using vfs.libarchive

file_listing = my_archive.list_all() #Lists all files in the archive

file_listing = my_archive.stat_all() #Dict of all files in the archive containing fullpath, filename, file size (extracted)

files_extracted, success_of_extraction = my_archive.extract()  #Extracts all files to directory_out, returns list of files extracted and True/False for extraction success.  Defaults to extract all files in the archive.
```
or
```
files_extracted, success_of_extraction = my_archive.extract(files_to_extract=file_listing[0])  #Extracts only the listed file(s) in the archive to directory_out, returns list of files extracted and True/False for extraction success
```
Additional functions:
```
my_archive.archive_file('myfile2.zip') #Updates the currently set archive

my_archive.directory_out('/my/output_directory2/') #Updates the currently set output directory

my_archive.files_to_extract([file_listing[0],file_listing[3]]) #Updates the currently set file(s) to extract from the archive
```

Use of vfs.rar 3.1 or greater (Kodi v19 or greater):

Edit:  Currently crashes Kodi, so not recommended

Almost all archives can be handled by vfs.libarchive.  The only exception found at this point are [solid RAR archives](https://www.winrar-france.fr/winrar_instructions_for_use/source/html/HELPArcSolid.htm) (see issue [here](https://github.com/xbmc/vfs.libarchive/issues/35))

You can set archive_tool to use vfs.rar in these cases with

```
#Sleep call is currently requried to avoid crashing Kodi
xbmc.sleep(1000)
xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Addons.SetAddonEnabled","params":{"addonid": "vfs.libarchive", "enabled": false} }') #Temporarily disable vfs.libarchive
xbmc.sleep(1000)
my_archive = archive_tool.archive_tool(archive_file = 'myfile.rar',directory_out = '/my/output_directory/', use_vfs_rar=True) #Current archive object using vfs.rar instead of vfs.libarchive

xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Addons.SetAddonEnabled","params":{"addonid": "vfs.libarchive", "enabled": true} }') #re-enable vfs.libarchive
xbmc.sleep(1000)
```


To test archive types, there is a test script for this module which can be run from the addon settings.  In Kodi, go to System>Addons>Manage Dependancies>archive_tool>Configure>Run Archive Test

That should return:
```
DEBUG: archive_tool:  Test started.
DEBUG: archive_tool:  Testing ...test.zip
DEBUG: archive_tool: set to use vfs.libarchive
DEBUG: archive_tool:  File listing:
                    archive://...test.zip/test/test1.txt
                    archive://...test.zip/test/test2.txt
                    archive://...test.zip/test/test2/test3.txt
                    archive://...test.zip/test/test2/test4.txt
DEBUG: archive_tool:  File Stats:
                    Fullpath: archive://...test.zip/test/test1.txt, Filename: test1.txt, Size: 14,
                    Fullpath: archive://...test.zip/test/test2.txt, Filename: test2.txt, Size: 14,
                    Fullpath: archive://...test.zip/test/test2/test3.txt, Filename: test3.txt, Size: 14,
                    Fullpath: archive://...test.zip/test/test2/test4.txt, Filename: test4.txt, Size: 14,
DEBUG: archive_tool:  File Extraction Starting
DEBUG: archive_tool: Created folder ...test_zip/test/ for archive ...test.zip
DEBUG: archive_tool: Extracted file test1.txt from archive archive://...test.zip/test/
DEBUG: archive_tool: Extracted file test2.txt from archive archive://...test.zip/test/
DEBUG: archive_tool: Created folder ...test_zip/test/test2/ for archive archive://...test.zip/test/
DEBUG: archive_tool: Extracted file test3.txt from archive archive://...test.zip/test/test2/
DEBUG: archive_tool: Extracted file test4.txt from archive archive://...test.zip/test/test2/
DEBUG: archive_tool:  Extraction success returned True for test_zip.  Files:
                    ...test_zip/test/test1.txt
                    ...test_zip/test/test2.txt
                    ...test_zip/test/test2/test3.txt
                    ...test_zip/test/test2/test4.txt
DEBUG: archive_tool:  test_zip folder deleted
DEBUG: archive_tool:  Testing ...test.7z
DEBUG: archive_tool: set to use vfs.libarchive
DEBUG: archive_tool:  File listing:
                    archive://...test.7z/test/test1.txt
                    archive://...test.7z/test/test2.txt
                    archive://...test.7z/test/test2/test3.txt
                    archive://...test.7z/test/test2/test4.txt
DEBUG: archive_tool:  File Stats:
                    Fullpath: archive://...test.7z/test/test1.txt, Filename: test1.txt, Size: 14,
                    Fullpath: archive://...test.7z/test/test2.txt, Filename: test2.txt, Size: 14,
                    Fullpath: archive://...test.7z/test/test2/test3.txt, Filename: test3.txt, Size: 14,
                    Fullpath: archive://...test.7z/test/test2/test4.txt, Filename: test4.txt, Size: 14,
DEBUG: archive_tool:  File Extraction Starting
DEBUG: archive_tool: Created folder ...test_7z/test/ for archive ...test.7z
DEBUG: archive_tool: Extracted file test1.txt from archive archive://...test.7z/test/
DEBUG: archive_tool: Extracted file test2.txt from archive archive://...test.7z/test/
DEBUG: archive_tool: Created folder ...test_7z/test/test2/ for archive archive://...test.7z/test/
DEBUG: archive_tool: Extracted file test3.txt from archive archive://...test.7z/test/test2/
DEBUG: archive_tool: Extracted file test4.txt from archive archive://...test.7z/test/test2/
DEBUG: archive_tool:  Extraction success returned True for test_7z.  Files:
                    ...test_7z/test/test1.txt
                    ...test_7z/test/test2.txt
                    ...test_7z/test/test2/test3.txt
                    ...test_7z/test/test2/test4.txt
DEBUG: archive_tool:  test_7z folder deleted
DEBUG: archive_tool:  Testing ...test.tar
DEBUG: archive_tool: set to use vfs.libarchive
DEBUG: archive_tool:  File listing:
                    archive://...test.tar/test/test1.txt
                    archive://...test.tar/test/test2.txt
                    archive://...test.tar/test/test2/test4.txt
                    archive://...test.tar/test/test2/test3.txt
DEBUG: archive_tool:  File Stats:
                    Fullpath: archive://...test.tar/test/test1.txt, Filename: test1.txt, Size: 14,
                    Fullpath: archive://...test.tar/test/test2.txt, Filename: test2.txt, Size: 14,
                    Fullpath: archive://...test.tar/test/test2/test4.txt, Filename: test4.txt, Size: 14,
                    Fullpath: archive://...test.tar/test/test2/test3.txt, Filename: test3.txt, Size: 14,
DEBUG: archive_tool:  File Extraction Starting
DEBUG: archive_tool: Created folder ...test_tar/test/ for archive ...test.tar
DEBUG: archive_tool: Extracted file test1.txt from archive archive://...test.tar/test/
DEBUG: archive_tool: Extracted file test2.txt from archive archive://...test.tar/test/
DEBUG: archive_tool: Created folder ...test_tar/test/test2/ for archive archive://...test.tar/test/
DEBUG: ------ Window Deinit (DialogAddonSettings.xml) ------
DEBUG: archive_tool: Extracted file test4.txt from archive archive://...test.tar/test/test2/
DEBUG: archive_tool: Extracted file test3.txt from archive archive://...test.tar/test/test2/
DEBUG: archive_tool:  Extraction success returned True for test_tar.  Files:
                    ...test_tar/test/test1.txt
                    ...test_tar/test/test2.txt
                    ...test_tar/test/test2/test4.txt
                    ...test_tar/test/test2/test3.txt
DEBUG: archive_tool:  test_tar folder deleted
DEBUG: archive_tool:  Testing ...test.bz2
DEBUG: archive_tool: set to use vfs.libarchive
DEBUG: archive_tool:  File listing:
                    archive://...test.bz2/test/test1.txt
                    archive://...test.bz2/test/test2.txt
                    archive://...test.bz2/test/test2/test4.txt
                    archive://...test.bz2/test/test2/test3.txt
DEBUG: archive_tool:  File Stats:
                    Fullpath: archive://...test.bz2/test/test1.txt, Filename: test1.txt, Size: 14,
                    Fullpath: archive://...test.bz2/test/test2.txt, Filename: test2.txt, Size: 14,
                    Fullpath: archive://...test.bz2/test/test2/test4.txt, Filename: test4.txt, Size: 14,
                    Fullpath: archive://...test.bz2/test/test2/test3.txt, Filename: test3.txt, Size: 14,
DEBUG: archive_tool:  File Extraction Starting
DEBUG: archive_tool: Created folder ...test_bz2/test/ for archive ...test.bz2
DEBUG: archive_tool: Extracted file test1.txt from archive archive://...test.bz2/test/
DEBUG: archive_tool: Extracted file test2.txt from archive archive://...test.bz2/test/
DEBUG: archive_tool: Created folder ...test_bz2/test/test2/ for archive archive://...test.bz2/test/
DEBUG: archive_tool: Extracted file test4.txt from archive archive://...test.bz2/test/test2/
DEBUG: archive_tool: Extracted file test3.txt from archive archive://...test.bz2/test/test2/
DEBUG: archive_tool:  Extraction success returned True for test_bz2.  Files:
                    ...test_bz2/test/test1.txt
                    ...test_bz2/test/test2.txt
                    ...test_bz2/test/test2/test4.txt
                    ...test_bz2/test/test2/test3.txt
DEBUG: archive_tool:  test_bz2 folder deleted
DEBUG: archive_tool:  Testing ...test.gz
DEBUG: archive_tool: set to use vfs.libarchive
DEBUG: archive_tool:  File listing:
                    archive://...test.gz/test/test1.txt
                    archive://...test.gz/test/test2.txt
                    archive://...test.gz/test/test2/test4.txt
                    archive://...test.gz/test/test2/test3.txt
DEBUG: archive_tool:  File Stats:
                    Fullpath: archive://...test.gz/test/test1.txt, Filename: test1.txt, Size: 14,
                    Fullpath: archive://...test.gz/test/test2.txt, Filename: test2.txt, Size: 14,
                    Fullpath: archive://...test.gz/test/test2/test4.txt, Filename: test4.txt, Size: 14,
                    Fullpath: archive://...test.gz/test/test2/test3.txt, Filename: test3.txt, Size: 14,
DEBUG: archive_tool:  File Extraction Starting
DEBUG: archive_tool: Created folder ...test_gz/test/ for archive ...test.gz
DEBUG: archive_tool: Extracted file test1.txt from archive archive://...test.gz/test/
DEBUG: archive_tool: Extracted file test2.txt from archive archive://...test.gz/test/
DEBUG: archive_tool: Created folder ...test_gz/test/test2/ for archive archive://...test.gz/test/
DEBUG: archive_tool: Extracted file test4.txt from archive archive://...test.gz/test/test2/
DEBUG: archive_tool: Extracted file test3.txt from archive archive://...test.gz/test/test2/
DEBUG: archive_tool:  Extraction success returned True for test_gz.  Files:
                    ...test_gz/test/test1.txt
                    ...test_gz/test/test2.txt
                    ...test_gz/test/test2/test4.txt
                    ...test_gz/test/test2/test3.txt
DEBUG: archive_tool:  test_gz folder deleted
DEBUG: archive_tool:  Testing ...test.xz
DEBUG: archive_tool: set to use vfs.libarchive
DEBUG: archive_tool:  File listing:
                    archive://...test.xz/test/test1.txt
                    archive://...test.xz/test/test2.txt
                    archive://...test.xz/test/test2/test4.txt
                    archive://...test.xz/test/test2/test3.txt
DEBUG: archive_tool:  File Stats:
                    Fullpath: archive://...test.xz/test/test1.txt, Filename: test1.txt, Size: 14,
                    Fullpath: archive://...test.xz/test/test2.txt, Filename: test2.txt, Size: 14,
                    Fullpath: archive://...test.xz/test/test2/test4.txt, Filename: test4.txt, Size: 14,
                    Fullpath: archive://...test.xz/test/test2/test3.txt, Filename: test3.txt, Size: 14,
DEBUG: archive_tool:  File Extraction Starting
DEBUG: archive_tool: Created folder ...test_xz/test/ for archive ...test.xz
DEBUG: archive_tool: Extracted file test1.txt from archive archive://...test.xz/test/
DEBUG: archive_tool: Extracted file test2.txt from archive archive://...test.xz/test/
DEBUG: archive_tool: Created folder ...test_xz/test/test2/ for archive archive://...test.xz/test/
DEBUG: archive_tool: Extracted file test4.txt from archive archive://...test.xz/test/test2/
DEBUG: archive_tool: Extracted file test3.txt from archive archive://...test.xz/test/test2/
DEBUG: archive_tool:  Extraction success returned True for test_xz.  Files:
                    ...test_xz/test/test1.txt
                    ...test_xz/test/test2.txt
                    ...test_xz/test/test2/test4.txt
                    ...test_xz/test/test2/test3.txt
DEBUG: archive_tool:  test_xz folder deleted
DEBUG: archive_tool:  Testing ...test.iso
DEBUG: archive_tool: set to use vfs.libarchive
DEBUG: archive_tool:  File listing:
                    archive://...test.iso/.
                    archive://...test.iso/test2
                    archive://...test.iso/test1.txt
                    archive://...test.iso/test2.txt
                    archive://...test.iso/test2/test4.txt
                    archive://...test.iso/test2/test3.txt
DEBUG: archive_tool:  File Stats:
                    Fullpath: archive://...test.iso/., Filename: ., Size: 2048,
                    Fullpath: archive://...test.iso/test2, Filename: test2, Size: 2048,
                    Fullpath: archive://...test.iso/test1.txt, Filename: test1.txt, Size: 14,
                    Fullpath: archive://...test.iso/test2.txt, Filename: test2.txt, Size: 14,
                    Fullpath: archive://...test.iso/test2/test4.txt, Filename: test4.txt, Size: 14,
                    Fullpath: archive://...test.iso/test2/test3.txt, Filename: test3.txt, Size: 14,
DEBUG: archive_tool:  File Extraction Starting
ERROR: archive_tool error:  Error extracting file . from archive ...test.iso
ERROR: archive_tool error:  Error extracting file test2 from archive ...test.iso
DEBUG: archive_tool: Extracted file test1.txt from archive ...test.iso
DEBUG: archive_tool: Extracted file test2.txt from archive ...test.iso
DEBUG: archive_tool: Created folder ...test_iso/test2/ for archive ...test.iso
DEBUG: archive_tool: Extracted file test4.txt from archive archive://...test.iso/test2/
DEBUG: archive_tool: Extracted file test3.txt from archive archive://...test.iso/test2/
DEBUG: archive_tool:  Extraction success returned False for test_iso.  Files:
                    ...test_iso/test1.txt
                    ...test_iso/test2.txt
                    ...test_iso/test2/test4.txt
                    ...test_iso/test2/test3.txt
DEBUG: archive_tool:  Testing with vfs.libarchive ...test.rar
DEBUG: archive_tool: set to use vfs.libarchive
DEBUG: archive_tool:  File listing:
                    archive://...test.rar/test/test1.txt
                    archive://...test.rar/test/test2.txt
                    archive://...test.rar/test/test_folder/test3.txt
                    archive://...test.rar/test/test_folder/test4.txt
DEBUG: archive_tool:  File Stats:
                    Fullpath: archive://...test.rar/test/test1.txt, Filename: test1.txt, Size: 14,
                    Fullpath: archive://...test.rar/test/test2.txt, Filename: test2.txt, Size: 14,
                    Fullpath: archive://...test.rar/test/test_folder/test3.txt, Filename: test3.txt, Size: 14,
                    Fullpath: archive://...test.rar/test/test_folder/test4.txt, Filename: test4.txt, Size: 14,
DEBUG: archive_tool:  File Extraction Starting
DEBUG: archive_tool: Created folder ...test_rar/test/ for archive ...test.rar
DEBUG: archive_tool: Extracted file test1.txt from archive archive://...test.rar/test/
DEBUG: archive_tool: Extracted file test2.txt from archive archive://...test.rar/test/
DEBUG: archive_tool: Created folder ...test_rar/test/test_folder/ for archive archive://...test.rar/test/
DEBUG: archive_tool: Extracted file test3.txt from archive archive://...test.rar/test/test_folder/
DEBUG: archive_tool: Extracted file test4.txt from archive archive://...test.rar/test/test_folder/
DEBUG: archive_tool:  Extraction success returned True for test_rar.  Files:
                    ...test_rar/test/test1.txt
                    ...test_rar/test/test2.txt
                    ...test_rar/test/test_folder/test3.txt
                    ...test_rar/test/test_folder/test4.txt
DEBUG: archive_tool:  test_rar folder deleted
DEBUG: archive_tool:  Testing with vfs.rar ...test.rar
DEBUG: archive_tool: set to use vfs.rar
DEBUG: archive_tool:  File listing:
                    rar://...test.rar/test/test1.txt
                    rar://...test.rar/test/test2.txt
                    rar://...test.rar/test/test_folder/test3.txt
                    rar://...test.rar/test/test_folder/test4.txt
DEBUG: archive_tool:  File Stats:
                    Fullpath: rar://...test.rar/test/test1.txt, Filename: test1.txt, Size: 14,
                    Fullpath: rar://...test.rar/test/test2.txt, Filename: test2.txt, Size: 14,
                    Fullpath: rar://...test.rar/test/test_folder/test3.txt, Filename: test3.txt, Size: 14,
                    Fullpath: rar://...test.rar/test/test_folder/test4.txt, Filename: test4.txt, Size: 14,
DEBUG: archive_tool:  File Extraction Starting
DEBUG: archive_tool: Created folder ...test_rar/test/ for archive ...test.rar
DEBUG: AddOnLog: RAR archive support: CRarFile::Read: Read reached end of file
DEBUG: archive_tool: Extracted file test1.txt from archive rar://...test.rar/test/
DEBUG: AddOnLog: RAR archive support: CRarFile::Read: Read reached end of file
DEBUG: archive_tool: Extracted file test2.txt from archive rar://...test.rar/test/
DEBUG: archive_tool: Created folder ...test_rar/test/test_folder/ for archive rar://...test.rar/test/
DEBUG: AddOnLog: RAR archive support: CRarFile::Read: Read reached end of file
DEBUG: archive_tool: Extracted file test3.txt from archive rar://...test.rar/test/test_folder/
DEBUG: AddOnLog: RAR archive support: CRarFile::Read: Read reached end of file
DEBUG: archive_tool: Extracted file test4.txt from archive rar://...test.rar/test/test_folder/
DEBUG: archive_tool:  Extraction success returned True for test_rar.  Files:
                    ...test_rar/test/test1.txt
                    ...test_rar/test/test2.txt
                    ...test_rar/test/test_folder/test3.txt
                    ...test_rar/test/test_folder/test4.txt
DEBUG: archive_tool:  test_rar folder deleted
DEBUG: archive_tool:  Testing ...example.rar
DEBUG: archive_tool: set to use vfs.rar
DEBUG: archive_tool:  File listing:
                    rar://...example.rar/ALITA - ANJO DE COMBATE/Alita.Battle.Angel.2019.PT.srt
                    rar://...example.rar/ALITA - ANJO DE COMBATE/WEB-DL/Alita Battle Angel 2019 1080p HDRip X264-EVO.srt
                    rar://...example.rar/ALITA - ANJO DE COMBATE/WEB-DL/Alita.Battle.Angel.2019.1080p.WEB-DL.H264.AC3-EVO.srt
                    rar://...example.rar/ALITA - ANJO DE COMBATE/WEB-DL/Alita.Battle.Angel.2019.V2.1080p.HDRip.X264-EVO.srt
                    rar://...example.rar/ALITA - ANJO DE COMBATE/HD/Alita.Battle.Angel.2019.720p.BluRay.x264-SPARKS.srt
DEBUG: archive_tool:  File Stats:
                    Fullpath: rar://...example.rar/ALITA - ANJO DE COMBATE/Alita.Battle.Angel.2019.PT.srt, Filename: Alita.Battle.Angel.2019.PT.srt, Size: 84918,
                    Fullpath: rar://...example.rar/ALITA - ANJO DE COMBATE/WEB-DL/Alita Battle Angel 2019 1080p HDRip X264-EVO.srt, Filename: Alita Battle Angel 2019 1080p HDRip X264-EVO.srt, Size: 84918,
                    Fullpath: rar://...example.rar/ALITA - ANJO DE COMBATE/WEB-DL/Alita.Battle.Angel.2019.1080p.WEB-DL.H264.AC3-EVO.srt, Filename: Alita.Battle.Angel.2019.1080p.WEB-DL.H264.AC3-EVO.srt, Size: 84918,
                    Fullpath: rar://...example.rar/ALITA - ANJO DE COMBATE/WEB-DL/Alita.Battle.Angel.2019.V2.1080p.HDRip.X264-EVO.srt, Filename: Alita.Battle.Angel.2019.V2.1080p.HDRip.X264-EVO.srt, Size: 84918,
                    Fullpath: rar://...example.rar/ALITA - ANJO DE COMBATE/HD/Alita.Battle.Angel.2019.720p.BluRay.x264-SPARKS.srt, Filename: Alita.Battle.Angel.2019.720p.BluRay.x264-SPARKS.srt, Size: 84918,
DEBUG: archive_tool:  File Extraction Starting
DEBUG: archive_tool: Created folder ...example_rar/ALITA - ANJO DE COMBATE/ for archive ...example.rar
DEBUG: archive_tool: Extracted file Alita.Battle.Angel.2019.PT.srt from archive rar://...example.rar/ALITA - ANJO DE COMBATE/
DEBUG: archive_tool: Created folder ...example_rar/ALITA - ANJO DE COMBATE/WEB-DL/ for archive rar://...example.rar/ALITA - ANJO DE COMBATE/
DEBUG: archive_tool: Extracted file Alita Battle Angel 2019 1080p HDRip X264-EVO.srt from archive rar://...example.rar/ALITA - ANJO DE COMBATE/WEB-DL/
DEBUG: archive_tool: Extracted file Alita.Battle.Angel.2019.1080p.WEB-DL.H264.AC3-EVO.srt from archive rar://...example.rar/ALITA - ANJO DE COMBATE/WEB-DL/
DEBUG: archive_tool: Extracted file Alita.Battle.Angel.2019.V2.1080p.HDRip.X264-EVO.srt from archive rar://...example.rar/ALITA - ANJO DE COMBATE/WEB-DL/
DEBUG: archive_tool: Created folder ...example_rar/ALITA - ANJO DE COMBATE/HD/ for archive rar://...example.rar/ALITA - ANJO DE COMBATE/
DEBUG: archive_tool: Extracted file Alita.Battle.Angel.2019.720p.BluRay.x264-SPARKS.srt from archive rar://...example.rar/ALITA - ANJO DE COMBATE/HD/
DEBUG: archive_tool:  Extraction success returned True for example_rar.  Files:
                    ...example_rar/ALITA - ANJO DE COMBATE/Alita.Battle.Angel.2019.PT.srt
                    ...example_rar/ALITA - ANJO DE COMBATE/WEB-DL/Alita Battle Angel 2019 1080p HDRip X264-EVO.srt
                    ...example_rar/ALITA - ANJO DE COMBATE/WEB-DL/Alita.Battle.Angel.2019.1080p.WEB-DL.H264.AC3-EVO.srt
                    ...example_rar/ALITA - ANJO DE COMBATE/WEB-DL/Alita.Battle.Angel.2019.V2.1080p.HDRip.X264-EVO.srt
                    ...example_rar/ALITA - ANJO DE COMBATE/HD/Alita.Battle.Angel.2019.720p.BluRay.x264-SPARKS.srt
DEBUG: archive_tool:  example_rar folder deleted
DEBUG: archive_tool:  Test completed
```
