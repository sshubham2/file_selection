from pathlib import Path
from datetime import datetime
import re

class LatestFile:
    
    def by_date(self, file_list: list):
        '''
        Read files names and return file having most recent date in the filename. If there are multiple files with same date in filename, most recent file is determined by
        create datetime. Date in filename must be in ddmmyyyy format.
        This function accepts a list of Path objects.
        '''
        files : list = []
        for file in file_list:
            files.append(str(file))

        dates : list = []
        for file in files:
            dates.append(datetime.strptime(re.search('(\d{8})',file).group(1),'%d%m%Y'))

        re_string = re.escape(max(dates).strftime('%d%m%Y'))
        r = re.compile(re_string)
        result_files = list(map(Path, list(filter(r.search, files))))

        if(len(result_files) > 1):
            most_recent_file = self.by_create_datetime(result_files)
            pass
        else:
            most_recent_file = result_files[0]
            
        return most_recent_file
    
    def by_create_datetime(self, file_list: list):
        '''
        Returns most recent file which is determined by create datetime.
        This function accepts list of Path objects.
        '''
        result_file =  [file for file in file_list if file.stat().st_ctime == max([file.stat().st_ctime for file in file_list])]
        if(len(result_file) > 1):
            print('2 or more files have same create datetime. Latest file will be selected randomly.\n Files - {}'.format(result_file))
            return result_file[0]
        else:
            return result_file[0]
    
    def by_version_number_decimal(self, file_list: list):
        '''
        Returns Path of file containing max version number. Version number in file name must be in decimal format.
        This function accepts a list of Path objects 
        '''
        version_numbers : list = []
        for file in file_list:
            version_numbers.append(re.search(r'v(\d+\.\d+)', str(file)).group(1))
        version_numbers = list(map(float, version_numbers))
        
        result_file =  [file for file in file_list if float(re.search(r'v(\d+\.\d+)', str(file)).group(1)) == max(version_numbers)]
        if(len(result_file) > 1):
            print('2 or more files have same version number. File will be selected randomly.\n Files - {}'.format(result_file))
            return result_file[0]
        else:
            return result_file[0]
    
    def by_version_number_integer(self, file_list: list):
        '''
        Returns Path of file containing max version number. Version number in file name must be in integer format.
        This function accepts a list of Path objects 
        '''
        version_numbers : list = []
        for file in file_list:
            version_numbers.append(re.search(r'v(\d+)', str(file)).group(1))
        version_numbers = list(map(int, version_numbers))

        result_file =  [file for file in file_list if int(re.search(r'v(\d+)', str(file)).group(1)) == max(version_numbers)]
        if(len(result_file) > 1):
            print('2 or more files have same version number. File will be selected randomly.\n Files - {}'.format(result_file))
            return result_file[0]
        else:
            return result_file[0]