# Automated Invoice Downloader

<a href="https://github.com/liamstrang/Invoice-Downloader/actions/workflows/test.yaml">
  <img src="https://github.com/liamstrang/Invoice-Downloader/actions/workflows/test.yaml/badge.svg" alt="Workflow status badge" height="20">
</a>

## Instructions

1. Download or Clone this repository
2. Edit `src/.env.example` and fill in the HOST (eg: imap.gmail.com), USER, PASS fields. Save the file and rename to `.env`
3. Install pip packages with `pip install -r requirements.txt` **(Requirements Python >3.6)**
4. Run `fetch.bat` in the home directory

## Usage

### Automatic Download
1. Open `fetch.bat`
2. Type the number of the corresponding supplier to download
3. Enter the start date (eg 14/04/2023)
4. Enter the end date (eg 23/04/2023)
5. Invoices will begin to download to `Downloads/*todaysDate*/*SupplierName*`

### Manual Download
1. Open `fetch.bat`
2. Type the number of the manual download
3. Type the invoice or PO number
5. Invoices will begin to download to `Downloads/manual/*SupplierName*`
