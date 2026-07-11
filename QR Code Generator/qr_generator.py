# import qrcode

def generate_qr(data, filename):
    print(f'Generating QR code for: {data}')
    # img = qrcode.make(data)
    # img.save(filename)
    print(f'QR code saved as {filename}')

if __name__ == '__main__':
    generate_qr('https://www.thaparsummerschool.com', 'tss_link.png')