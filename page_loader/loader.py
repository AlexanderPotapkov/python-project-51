from page_loader.file_manager import check_output_dir, create_dir_for_files, save_file
from page_loader.name import get_dir_name, get_html_name, get_path
from page_loader.web_manager import download_resources, get_response, get_soup


def download(url, output):
    check_output_dir(output)
    path_to_output_file = get_path(output, get_html_name(url))
    path_to_files_dir = get_path(output, get_dir_name(url))
    raw_response = get_response(url)
    soup = get_soup(raw_response)
    create_dir_for_files(path_to_files_dir)
    download_resources(url, soup, path_to_files_dir)
    save_file(path_to_output_file, soup.prettify())
    return f'{path_to_output_file}\n'f'{path_to_files_dir}'
