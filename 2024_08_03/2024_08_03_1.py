from datetime import datetime
import file




def main():
    now = datetime.now()
    current_file_name = now.strftime('%Y_%m_%d.log')
    log_path = file.created_log_file(current_file_name)
    file.record_info(log_path)
    
    


if __name__ == '__main__':
    main()