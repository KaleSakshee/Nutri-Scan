def parse_barcode(barcode):
    dummy_barcode_map = {
        "123456789": "KitKat",
        "987654321": "Peanut Butter",
        "111222333": "Dark Chocolate"
    }

    return dummy_barcode_map.get(barcode)
