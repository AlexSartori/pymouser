# PyMouser

## Installation

Install the package with pip.

```pip install --user pymouser```

## Usage:

```python
import pymouser


# Initialize the package with your API key
mouser = pymouser.MouserAPI('your-search-key')

# Search by Part-Number
err, res = mouser.search_by_PN('your-part-number')

# Check for errors or print the returned results
if err:
    print("Error during request:")
    print(err)
else:
    if res['NumberOfResult'] == 0:
        print("No results matched the part number")
    else:
        for match in res['Parts']:
            print("Match for PartNumber .... %s" % match['MouserPartNumber'])
            print("Description ............. %s" % match['Description'])
            print("Link to datasheet ....... %s" % match['DataSheetUrl'])
            print("Link to product page .... %s" % match['ProductDetailUrl'])
            print("")
```