import tabula

# Read pdf into list of DataFrame
df = tabula.read_pdf("input.pdf", pages='all')

# convert PDF into CSV file
tabula.convert_into("input.pdf", "output.csv", output_format="csv", pages='all')
