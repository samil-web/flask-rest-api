from src.server import application
from src.utils import create_csv_file_if_not_exists


if __name__ == '__main__':
    create_csv_file_if_not_exists()
    application.run(debug=True)