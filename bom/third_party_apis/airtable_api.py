import logging

from airtable import Airtable


logger = logging.getLogger(__name__)

# Base ID's
OPERATIONS_ID = "appJfMcqGXNaYKRvw"


def get_manufacturer_id(name):
    """
    Get the Manufacturer ID for a given name

    If the manfacturer doesn't exist, create it
    """
    manufacturers = Airtable(OPERATIONS_ID, "Manufacturers")
    results = manufacturers.search("Name", name)
    if len(results) == 0:
        # Create manufacturer
        result = manufacturers.insert({
            "Name": name
        })
        return result['id']
    else:
        return results[0]['id']


def get_supplier_id(name):
    """
    Get the Supplier ID for a given name

    If the supplier doesn't exist, create it
    """
    suppliers = Airtable(OPERATIONS_ID, "Suppliers")
    results = suppliers.search("Name", name)
    if len(results) == 0:
        # Create supplier
        result = suppliers.insert({
            "Name": name
        })
        return result['id']
    else:
        return results[0]['id']


def add_mfg_part(mfg_part):
    """
    Add a manufacturer part to the Manufacturer Parts table in airtable
    """
    mfg_id = get_manufacturer_id(mfg_part.manufacturer.name)
    part_number = mfg_part.manufacturer_part_number

    manufacturer_parts = Airtable(OPERATIONS_ID, "Manufacturer Parts")

    # Check if the part already exists
    results = manufacturer_parts.search("Part Number", part_number)
    if len(results) != 0:
        return results[0]['id']

    result = manufacturer_parts.insert({
        "Part Number": part_number,
        "Manufacturer": [
            mfg_id
        ]
    })

    return result["id"]


def add_part(part):
    """
    Add a part to the Inventory table in airtable
    """
    # Get manufacturer and manfacturer part information
    mfg_parts = []
    for mfg_part in part.manufacturer_parts():
        mfg_part_id = add_mfg_part(mfg_part)
        if mfg_part_id not in mfg_parts:
            mfg_parts.append(mfg_part_id)

    # Get supplier and supplier part information
    suppliers = []
    for supplier_part in part.seller_parts():
        supplier_id = get_supplier_id(supplier_part.seller.name)
        if supplier_id not in suppliers:
            suppliers.append(supplier_id)

    part_info = {
        "Part Number": part.full_part_number(),
        "Description": part.description(),
        "Manufacturer Part": mfg_parts,
        "Supplier": suppliers
    }

    inventory = Airtable(OPERATIONS_ID, "Inventory")
    # Check if part has already been added
    results = inventory.search("Part Number", part.full_part_number())
    if len(results) == 0:
        result = inventory.insert(part_info)
    else:
        result = inventory.update(results[0]['id'], part_info)

    return result['id']

