from datetime import datetime
from tools.file import created_log_file,record_info




def main():
    now = datetime.now()
    current_file_name = now.strftime('%Y_%m_%d.log')
    log_path = created_log_file(current_file_name)
    record_info(log_path)
    
    


if __name__ == '__main__':
    main()