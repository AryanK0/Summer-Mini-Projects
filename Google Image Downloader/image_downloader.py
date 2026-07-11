# from bing_image_downloader import downloader

def download_images(query, limit):
    print(f'Downloading {limit} images for query: "{query}"')
    # downloader.download(query, limit=limit, output_dir='dataset', adult_filter_off=True)
    print('Download complete. Check the dataset directory.')

if __name__ == '__main__':
    download_images('golden retriever', 5)