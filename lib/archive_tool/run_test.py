from kodi_six import xbmc, xbmcaddon, xbmcgui, xbmcvfs
from kodi_six.utils import py2_encode, py2_decode
import os
import archive_tool

WIN = xbmcgui.Window(10000)
if not WIN.getProperty('archive_tool.script_started'):
	delete_files_after_extraction = True
	current_dialog = xbmcgui.Dialog()
	WIN.setProperty('archive_tool.script_started','True')
	xbmc.log(msg='archive_tool:  Test started.', level=xbmc.LOGDEBUG)
	addon_name = 'script.module.archive_tool'
	addon_handle = xbmcaddon.Addon(id='%(addon_name)s' % {'addon_name':addon_name})

	#Zip Test
	try:
		archive_file =  os.path.join(xbmc.translatePath(addon_handle.getAddonInfo('path')),'resources','test.zip')
		test_folder = os.path.join(xbmc.translatePath(addon_handle.getAddonInfo('path')),'resources','test_zip','')
		xbmc.log(msg='archive_tool:  Testing %(archive_file)s' % {'archive_file':archive_file}, level=xbmc.LOGDEBUG)
		my_archive = archive_tool.archive_tool(archive_file = archive_file,directory_out = test_folder) #Current archive object using vfs.libarchive
		file_listing = my_archive.list_all() #Lists all files in the archive
		xbmc.log(msg='archive_tool:  File listing:\n%(file_listing)s' % {'file_listing':'\n'.join(file_listing)}, level=xbmc.LOGDEBUG)
		stat_listing = my_archive.stat_all() #Dict of all files in the archive containing fullpath, filename, file size (extracted)
		xbmc.log(msg='archive_tool:  File Stats:\n%(stat_listing)s' % {'stat_listing':'\n'.join(['Fullpath: %(file_fp)s, Filename: %(file_fn)s, Size: %(file_s)s,'%{'file_fp':x['fullpath'],'file_fn':x['filename'],'file_s':x['size']} for x in stat_listing])}, level=xbmc.LOGDEBUG)
		xbmc.log(msg='archive_tool:  File Extraction Starting', level=xbmc.LOGDEBUG)
		files_extracted, success_of_extraction = my_archive.extract()  #Extracts all files to directory_out, returns list of files extracted and True/False for extraction success.  Defaults to extract all files in the archive.
		xbmc.log(msg='archive_tool:  Extraction success returned %(ex_success)s for test_zip.  Files:\n%(file_listing)s' % {'ex_success':success_of_extraction,'file_listing':'\n'.join(files_extracted)}, level=xbmc.LOGDEBUG)
		if success_of_extraction and delete_files_after_extraction:
			if xbmcvfs.rmdir(test_folder,True):
				xbmc.log(msg='archive_tool:  test_zip folder deleted', level=xbmc.LOGDEBUG)
	except Exception as exc:
		xbmc.log(msg='archive_tool:  Error in test_zip.  Exception %(exc)s' % {'exc': exc}, level=xbmc.LOGERROR)
 
 	#7z Test
	try:
		archive_file =  os.path.join(xbmc.translatePath(addon_handle.getAddonInfo('path')),'resources','test.7z')
		test_folder = os.path.join(xbmc.translatePath(addon_handle.getAddonInfo('path')),'resources','test_7z','')
		xbmc.log(msg='archive_tool:  Testing %(archive_file)s' % {'archive_file':archive_file}, level=xbmc.LOGDEBUG)
		my_archive = archive_tool.archive_tool(archive_file = archive_file,directory_out = test_folder) #Current archive object using vfs.libarchive
		file_listing = my_archive.list_all() #Lists all files in the archive
		xbmc.log(msg='archive_tool:  File listing:\n%(file_listing)s' % {'file_listing':'\n'.join(file_listing)}, level=xbmc.LOGDEBUG)
		stat_listing = my_archive.stat_all() #Dict of all files in the archive containing fullpath, filename, file size (extracted)
		xbmc.log(msg='archive_tool:  File Stats:\n%(stat_listing)s' % {'stat_listing':'\n'.join(['Fullpath: %(file_fp)s, Filename: %(file_fn)s, Size: %(file_s)s,'%{'file_fp':x['fullpath'],'file_fn':x['filename'],'file_s':x['size']} for x in stat_listing])}, level=xbmc.LOGDEBUG)
		xbmc.log(msg='archive_tool:  File Extraction Starting', level=xbmc.LOGDEBUG)
		files_extracted, success_of_extraction = my_archive.extract()  #Extracts all files to directory_out, returns list of files extracted and True/False for extraction success.  Defaults to extract all files in the archive.
		xbmc.log(msg='archive_tool:  Extraction success returned %(ex_success)s for test_7z.  Files:\n%(file_listing)s' % {'ex_success':success_of_extraction,'file_listing':'\n'.join(files_extracted)}, level=xbmc.LOGDEBUG)
		if success_of_extraction and delete_files_after_extraction:
			if xbmcvfs.rmdir(test_folder,True):
				xbmc.log(msg='archive_tool:  test_7z folder deleted', level=xbmc.LOGDEBUG)
	except Exception as exc:
		xbmc.log(msg='archive_tool:  Error in test_7z.  Exception %(exc)s' % {'exc': exc}, level=xbmc.LOGERROR)

 	#tar Test
	try:
		archive_file =  os.path.join(xbmc.translatePath(addon_handle.getAddonInfo('path')),'resources','test.tar')
		test_folder = os.path.join(xbmc.translatePath(addon_handle.getAddonInfo('path')),'resources','test_tar','')
		xbmc.log(msg='archive_tool:  Testing %(archive_file)s' % {'archive_file':archive_file}, level=xbmc.LOGDEBUG)
		my_archive = archive_tool.archive_tool(archive_file = archive_file,directory_out = test_folder) #Current archive object using vfs.libarchive
		file_listing = my_archive.list_all() #Lists all files in the archive
		xbmc.log(msg='archive_tool:  File listing:\n%(file_listing)s' % {'file_listing':'\n'.join(file_listing)}, level=xbmc.LOGDEBUG)
		stat_listing = my_archive.stat_all() #Dict of all files in the archive containing fullpath, filename, file size (extracted)
		xbmc.log(msg='archive_tool:  File Stats:\n%(stat_listing)s' % {'stat_listing':'\n'.join(['Fullpath: %(file_fp)s, Filename: %(file_fn)s, Size: %(file_s)s,'%{'file_fp':x['fullpath'],'file_fn':x['filename'],'file_s':x['size']} for x in stat_listing])}, level=xbmc.LOGDEBUG)
		xbmc.log(msg='archive_tool:  File Extraction Starting', level=xbmc.LOGDEBUG)
		files_extracted, success_of_extraction = my_archive.extract()  #Extracts all files to directory_out, returns list of files extracted and True/False for extraction success.  Defaults to extract all files in the archive.
		xbmc.log(msg='archive_tool:  Extraction success returned %(ex_success)s for test_tar.  Files:\n%(file_listing)s' % {'ex_success':success_of_extraction,'file_listing':'\n'.join(files_extracted)}, level=xbmc.LOGDEBUG)
		if success_of_extraction and delete_files_after_extraction:
			if xbmcvfs.rmdir(test_folder,True):
				xbmc.log(msg='archive_tool:  test_tar folder deleted', level=xbmc.LOGDEBUG)
	except Exception as exc:
		xbmc.log(msg='archive_tool:  Error in test_tar.  Exception %(exc)s' % {'exc': exc}, level=xbmc.LOGERROR)

 	#bz2 Test
	try:
		archive_file =  os.path.join(xbmc.translatePath(addon_handle.getAddonInfo('path')),'resources','test.bz2')
		test_folder = os.path.join(xbmc.translatePath(addon_handle.getAddonInfo('path')),'resources','test_bz2','')
		xbmc.log(msg='archive_tool:  Testing %(archive_file)s' % {'archive_file':archive_file}, level=xbmc.LOGDEBUG)
		my_archive = archive_tool.archive_tool(archive_file = archive_file,directory_out = test_folder) #Current archive object using vfs.libarchive
		file_listing = my_archive.list_all() #Lists all files in the archive
		xbmc.log(msg='archive_tool:  File listing:\n%(file_listing)s' % {'file_listing':'\n'.join(file_listing)}, level=xbmc.LOGDEBUG)
		stat_listing = my_archive.stat_all() #Dict of all files in the archive containing fullpath, filename, file size (extracted)
		xbmc.log(msg='archive_tool:  File Stats:\n%(stat_listing)s' % {'stat_listing':'\n'.join(['Fullpath: %(file_fp)s, Filename: %(file_fn)s, Size: %(file_s)s,'%{'file_fp':x['fullpath'],'file_fn':x['filename'],'file_s':x['size']} for x in stat_listing])}, level=xbmc.LOGDEBUG)
		xbmc.log(msg='archive_tool:  File Extraction Starting', level=xbmc.LOGDEBUG)
		files_extracted, success_of_extraction = my_archive.extract()  #Extracts all files to directory_out, returns list of files extracted and True/False for extraction success.  Defaults to extract all files in the archive.
		xbmc.log(msg='archive_tool:  Extraction success returned %(ex_success)s for test_bz2.  Files:\n%(file_listing)s' % {'ex_success':success_of_extraction,'file_listing':'\n'.join(files_extracted)}, level=xbmc.LOGDEBUG)
		if success_of_extraction and delete_files_after_extraction:
			if xbmcvfs.rmdir(test_folder,True):
				xbmc.log(msg='archive_tool:  test_bz2 folder deleted', level=xbmc.LOGDEBUG)
	except Exception as exc:
		xbmc.log(msg='archive_tool:  Error in test_bz2.  Exception %(exc)s' % {'exc': exc}, level=xbmc.LOGERROR)

 	#gz Test
	try:
		archive_file =  os.path.join(xbmc.translatePath(addon_handle.getAddonInfo('path')),'resources','test.gz')
		test_folder = os.path.join(xbmc.translatePath(addon_handle.getAddonInfo('path')),'resources','test_gz','')
		xbmc.log(msg='archive_tool:  Testing %(archive_file)s' % {'archive_file':archive_file}, level=xbmc.LOGDEBUG)
		my_archive = archive_tool.archive_tool(archive_file = archive_file,directory_out = test_folder) #Current archive object using vfs.libarchive
		file_listing = my_archive.list_all() #Lists all files in the archive
		xbmc.log(msg='archive_tool:  File listing:\n%(file_listing)s' % {'file_listing':'\n'.join(file_listing)}, level=xbmc.LOGDEBUG)
		stat_listing = my_archive.stat_all() #Dict of all files in the archive containing fullpath, filename, file size (extracted)
		xbmc.log(msg='archive_tool:  File Stats:\n%(stat_listing)s' % {'stat_listing':'\n'.join(['Fullpath: %(file_fp)s, Filename: %(file_fn)s, Size: %(file_s)s,'%{'file_fp':x['fullpath'],'file_fn':x['filename'],'file_s':x['size']} for x in stat_listing])}, level=xbmc.LOGDEBUG)
		xbmc.log(msg='archive_tool:  File Extraction Starting', level=xbmc.LOGDEBUG)
		files_extracted, success_of_extraction = my_archive.extract()  #Extracts all files to directory_out, returns list of files extracted and True/False for extraction success.  Defaults to extract all files in the archive.
		xbmc.log(msg='archive_tool:  Extraction success returned %(ex_success)s for test_gz.  Files:\n%(file_listing)s' % {'ex_success':success_of_extraction,'file_listing':'\n'.join(files_extracted)}, level=xbmc.LOGDEBUG)
		if success_of_extraction and delete_files_after_extraction:
			if xbmcvfs.rmdir(test_folder,True):
				xbmc.log(msg='archive_tool:  test_gz folder deleted', level=xbmc.LOGDEBUG)
	except Exception as exc:
		xbmc.log(msg='archive_tool:  Error in test_gz.  Exception %(exc)s' % {'exc': exc}, level=xbmc.LOGERROR)

 	#xz Test
	try:
		archive_file =  os.path.join(xbmc.translatePath(addon_handle.getAddonInfo('path')),'resources','test.xz')
		test_folder = os.path.join(xbmc.translatePath(addon_handle.getAddonInfo('path')),'resources','test_xz','')
		xbmc.log(msg='archive_tool:  Testing %(archive_file)s' % {'archive_file':archive_file}, level=xbmc.LOGDEBUG)
		my_archive = archive_tool.archive_tool(archive_file = archive_file,directory_out = test_folder) #Current archive object using vfs.libarchive
		file_listing = my_archive.list_all() #Lists all files in the archive
		xbmc.log(msg='archive_tool:  File listing:\n%(file_listing)s' % {'file_listing':'\n'.join(file_listing)}, level=xbmc.LOGDEBUG)
		stat_listing = my_archive.stat_all() #Dict of all files in the archive containing fullpath, filename, file size (extracted)
		xbmc.log(msg='archive_tool:  File Stats:\n%(stat_listing)s' % {'stat_listing':'\n'.join(['Fullpath: %(file_fp)s, Filename: %(file_fn)s, Size: %(file_s)s,'%{'file_fp':x['fullpath'],'file_fn':x['filename'],'file_s':x['size']} for x in stat_listing])}, level=xbmc.LOGDEBUG)
		xbmc.log(msg='archive_tool:  File Extraction Starting', level=xbmc.LOGDEBUG)
		files_extracted, success_of_extraction = my_archive.extract()  #Extracts all files to directory_out, returns list of files extracted and True/False for extraction success.  Defaults to extract all files in the archive.
		xbmc.log(msg='archive_tool:  Extraction success returned %(ex_success)s for test_xz.  Files:\n%(file_listing)s' % {'ex_success':success_of_extraction,'file_listing':'\n'.join(files_extracted)}, level=xbmc.LOGDEBUG)
		if success_of_extraction and delete_files_after_extraction:
			if xbmcvfs.rmdir(test_folder,True):
				xbmc.log(msg='archive_tool:  test_xz folder deleted', level=xbmc.LOGDEBUG)
	except Exception as exc:
		xbmc.log(msg='archive_tool:  Error in test_xz.  Exception %(exc)s' % {'exc': exc}, level=xbmc.LOGERROR)

 	#iso Test
	try:
		archive_file =  os.path.join(xbmc.translatePath(addon_handle.getAddonInfo('path')),'resources','test.iso')
		test_folder = os.path.join(xbmc.translatePath(addon_handle.getAddonInfo('path')),'resources','test_iso','')
		xbmc.log(msg='archive_tool:  Testing %(archive_file)s' % {'archive_file':archive_file}, level=xbmc.LOGDEBUG)
		my_archive = archive_tool.archive_tool(archive_file = archive_file,directory_out = test_folder) #Current archive object using vfs.libarchive
		file_listing = my_archive.list_all() #Lists all files in the archive
		xbmc.log(msg='archive_tool:  File listing:\n%(file_listing)s' % {'file_listing':'\n'.join(file_listing)}, level=xbmc.LOGDEBUG)
		stat_listing = my_archive.stat_all() #Dict of all files in the archive containing fullpath, filename, file size (extracted)
		xbmc.log(msg='archive_tool:  File Stats:\n%(stat_listing)s' % {'stat_listing':'\n'.join(['Fullpath: %(file_fp)s, Filename: %(file_fn)s, Size: %(file_s)s,'%{'file_fp':x['fullpath'],'file_fn':x['filename'],'file_s':x['size']} for x in stat_listing])}, level=xbmc.LOGDEBUG)
		xbmc.log(msg='archive_tool:  File Extraction Starting', level=xbmc.LOGDEBUG)
		files_extracted, success_of_extraction = my_archive.extract()  #Extracts all files to directory_out, returns list of files extracted and True/False for extraction success.  Defaults to extract all files in the archive.
		xbmc.log(msg='archive_tool:  Extraction success returned %(ex_success)s for test_iso.  Files:\n%(file_listing)s' % {'ex_success':success_of_extraction,'file_listing':'\n'.join(files_extracted)}, level=xbmc.LOGDEBUG)
		if success_of_extraction and delete_files_after_extraction:
			if xbmcvfs.rmdir(test_folder,True):
				xbmc.log(msg='archive_tool:  test_iso folder deleted', level=xbmc.LOGDEBUG)
	except Exception as exc:
		xbmc.log(msg='archive_tool:  Error in test_iso.  Exception %(exc)s' % {'exc': exc}, level=xbmc.LOGERROR)

 	#rar (non solid) Test
	try:
		archive_file =  os.path.join(xbmc.translatePath(addon_handle.getAddonInfo('path')),'resources','test.rar')
		test_folder = os.path.join(xbmc.translatePath(addon_handle.getAddonInfo('path')),'resources','test_rar','')
		xbmc.log(msg='archive_tool:  Testing %(archive_file)s' % {'archive_file':archive_file}, level=xbmc.LOGDEBUG)
		my_archive = archive_tool.archive_tool(archive_file = archive_file,directory_out = test_folder) #Current archive object using vfs.libarchive
		file_listing = my_archive.list_all() #Lists all files in the archive
		xbmc.log(msg='archive_tool:  File listing:\n%(file_listing)s' % {'file_listing':'\n'.join(file_listing)}, level=xbmc.LOGDEBUG)
		stat_listing = my_archive.stat_all() #Dict of all files in the archive containing fullpath, filename, file size (extracted)
		xbmc.log(msg='archive_tool:  File Stats:\n%(stat_listing)s' % {'stat_listing':'\n'.join(['Fullpath: %(file_fp)s, Filename: %(file_fn)s, Size: %(file_s)s,'%{'file_fp':x['fullpath'],'file_fn':x['filename'],'file_s':x['size']} for x in stat_listing])}, level=xbmc.LOGDEBUG)
		xbmc.log(msg='archive_tool:  File Extraction Starting', level=xbmc.LOGDEBUG)
		files_extracted, success_of_extraction = my_archive.extract()  #Extracts all files to directory_out, returns list of files extracted and True/False for extraction success.  Defaults to extract all files in the archive.
		xbmc.log(msg='archive_tool:  Extraction success returned %(ex_success)s for test_rar.  Files:\n%(file_listing)s' % {'ex_success':success_of_extraction,'file_listing':'\n'.join(files_extracted)}, level=xbmc.LOGDEBUG)
		if success_of_extraction and delete_files_after_extraction:
			if xbmcvfs.rmdir(test_folder,True):
				xbmc.log(msg='archive_tool:  test_rar folder deleted', level=xbmc.LOGDEBUG)
	except Exception as exc:
		xbmc.log(msg='archive_tool:  Error in test_rar.  Exception %(exc)s' % {'exc': exc}, level=xbmc.LOGERROR)

 	#rar (solid) Test, currently crashes Kodi
	# xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Addons.SetAddonEnabled","params":{"addonid": "vfs.libarchive", "enabled": false} }') #Temporarily disable vfs.libarchive
	# xbmc.sleep(1)
	# try:
	# 	archive_file =  os.path.join(xbmc.translatePath(addon_handle.getAddonInfo('path')),'resources','example.rar')
	# 	test_folder = os.path.join(xbmc.translatePath(addon_handle.getAddonInfo('path')),'resources','example_rar','')
	# 	xbmc.log(msg='archive_tool:  Testing %(archive_file)s' % {'archive_file':archive_file}, level=xbmc.LOGDEBUG)
	# 	my_archive = archive_tool.archive_tool(archive_file = archive_file,directory_out = test_folder, use_vfs_rar=True) #Current archive object using vfs.libarchive
	# 	file_listing = my_archive.list_all() #Lists all files in the archive
	# 	xbmc.log(msg='archive_tool:  File listing:\n%(file_listing)s' % {'file_listing':'\n'.join(file_listing)}, level=xbmc.LOGDEBUG)
	# 	stat_listing = my_archive.stat_all() #Dict of all files in the archive containing fullpath, filename, file size (extracted)
	# 	xbmc.log(msg='archive_tool:  File Stats:\n%(stat_listing)s' % {'stat_listing':'\n'.join(['Fullpath: %(file_fp)s, Filename: %(file_fn)s, Size: %(file_s)s,'%{'file_fp':x['fullpath'],'file_fn':x['filename'],'file_s':x['size']} for x in stat_listing])}, level=xbmc.LOGDEBUG)
	# 	xbmc.log(msg='archive_tool:  File Extraction Starting', level=xbmc.LOGDEBUG)
	# 	files_extracted, success_of_extraction = my_archive.extract()  #Extracts all files to directory_out, returns list of files extracted and True/False for extraction success.  Defaults to extract all files in the archive.
	# 	xbmc.log(msg='archive_tool:  Extraction success returned %(ex_success)s for example_rar.  Files:\n%(file_listing)s' % {'ex_success':success_of_extraction,'file_listing':'\n'.join(files_extracted)}, level=xbmc.LOGDEBUG)
	# 	if success_of_extraction and delete_files_after_extraction:
	# 		if xbmcvfs.rmdir(test_folder,True):
	# 			xbmc.log(msg='archive_tool:  example_rar folder deleted', level=xbmc.LOGDEBUG)
	# except Exception as exc:
	# 	xbmc.log(msg='archive_tool:  Error in example_rar.  Exception %(exc)s' % {'exc': exc}, level=xbmc.LOGERROR)
	# xbmc.sleep(1)
	# xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Addons.SetAddonEnabled","params":{"addonid": "vfs.libarchive", "enabled": true} }') #Temporarily disable vfs.libarchive


	ok_ret = current_dialog.ok('Test Complete','Test Completed.  Check your debug log for results.')
	WIN.clearProperty('archive_tool.script_started')
	xbmc.log(msg='archive_tool:  Test completed', level=xbmc.LOGDEBUG)
else:
	xbmc.log(msg='archive_tool:  Test already running', level=xbmc.LOGDEBUG)