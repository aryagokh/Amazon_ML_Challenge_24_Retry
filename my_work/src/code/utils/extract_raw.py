import re

formal_unit = {
    'centimetre': 'centimetre',
    'cm': 'centimetre',
    'cms': 'centimetre',
    'centimetres': 'centimetre',
    'centimeter': 'centimetre',
    'centimeters': 'centimetre',
    'centimet': 'centimetre',
    'centime': 'centimetre',
    'cent': 'centimetre',
    'centimete': 'centimetre',

    'foot': 'foot',
    'feet': 'foot',
    'ft': 'foot',
    "'": 'foot',

    'millimetre': 'millimetre',
    'mm': 'millimetre',
    'mms': 'millimetre',
    'millimetres': 'millimetre',
    'millimeter': 'millimetre',
    'millimeters': 'millimetre',
    'millimet': 'millimetre',

    'metre': 'metre',
    'm': 'metre',
    'mtr': 'metre',
    'metres': 'metre',
    'meter': 'metre',
    'meters': 'metre',
    'met': 'metre',

    'inch': 'inch',
    'inches': 'inch',
    'inchs': 'inch',
    'in': 'inch',
    '"': 'inch',
    "''": 'inch',

    'yard': 'yard',
    'yards': 'yard',
    'yd': 'yard',
    'yds': 'yard',

    'milligram': 'milligram',
    'milligrams': 'milligram',
    'mg': 'milligram',
    'mgs': 'milligram',
    'millig': 'milligram',
    'milligm': 'milligram',
    'milligms': 'milligram',

    'kilogram': 'kilogram',
    'kilograms': 'kilogram',
    'kilog': 'kilogram',
    'kilogm': 'kilogram',
    'kilogms': 'kilogram',
    'kg': 'kilogram',
    'kgs': 'kilogram',

    'microgram':  'microgram',
    'micrograms':  'microgram',
    'microgm':  'microgram',
    'microgms':  'microgram',
    'ug':  'microgram',
    'µg':  'microgram',

    'gram': 'gram',
    'grams': 'gram',
    'g': 'gram',
    'gm': 'gram',
    'gms': 'gram',
    'gsm': 'gram',

    'ounce': 'ounce',
    'ounces': 'ounce',
    'oz': 'ounce',
    'ozs': 'ounce',

    'ton': 'ton',
    'tons': 'ton',
    'tonne': 'ton',
    'tonnes': 'ton',

    'pound': 'pound',
    'pounds': 'pound',
    'lb': 'pound',
    'lbs': 'pound',

    'millivolt': 'millivolt',
    'millivolts': 'millivolt',
    'milliv': 'millivolt',
    'mv': 'millivolt',

    'volt': 'volt',
    'volts': 'volt',
    'v': 'volt',

    'kilovolt': 'kilovolt',
    'kilovolts': 'kilovolt',
    'kilov': 'kilovolt',
    'kv': 'kilovolt',

    'watt': 'watt',
    'watts': 'watt',
    'w': 'watt',

    'kilowatt': 'kilowatt',
    'kilowatts': 'kilowatt',
    'kw': 'kilowatt',

    'cubic': 'cubic',
    'cu': 'cubic',
    'cb': 'cubic',
    'cub': 'cubic',
    'cubic foot': 'cubic foot',
    'cubic feet': 'cubic foot',
    'cu ft': 'cubic foot',
    'ft³': 'cubic foot',

    'microlitre': 'microlitre',
    'microlitres': 'microlitre',
    'microlit': 'microlitre',
    'microliter': 'microlitre',
    'microliters': 'microlitre',
    'µL': 'microlitre',
    'ul': 'microlitre',

    'cup': 'cup',
    'cups': 'cup',
    'cp': 'cup',
    'cps': 'cup',

    'fluid': 'fluid',
    'fluid ounce': 'fluid ounce',
    'fluid ounces': 'fluid ounce',
    'fl oz': 'fluid ounce',
    'fl ozs': 'fluid ounce',

    'centilitre': 'centilitre',
    'centilitres': 'centilitre',
    'centilit': 'centilitre',
    'centiliter': 'centilitre',
    'centiliters': 'centilitre',
    'cl': 'centilitre',

    'imp': 'imp',
    'imperial': 'imp',
    'imperial gallon': 'imperial gallon',
    'imperial gallons': 'imperial gallon',
    'imp gal': 'imperial gallon',

    'pint': 'pint',
    'pints': 'pint',
    'pt': 'pint',

    'decilitre': 'decilitre',
    'decilit': 'decilitre',
    'decilitres': 'decilitre',
    'deciliter': 'decilitre',
    'deciliters': 'decilitre',
    'dl': 'decilitre',

    'litre': 'litre',
    'litres': 'litre',
    'liter': 'litre',
    'liters': 'litre',
    'l': 'litre',
    'ltr': 'litre',
    'ltrs': 'litre',

    'millilitre': 'millilitre',
    'millilitres': 'millilitre',
    'milliliter': 'millilitre',
    'milliliters': 'millilitre',
    'millilit': 'millilitre',
    'mlltr': 'millilitre',
    'milliltr': 'millilitre',
    'ml': 'millilitre',

    'quart': 'quart',
    'quarts': 'quart',
    'qt': 'quart',

    'cubic': 'cubic',
    'cu': 'cubic',
    'cb': 'cubic',
    'cub': 'cubic',
    'cubic inch': 'cubic inch',
    'cubic inches': 'cubic inch',
    'cu in': 'cubic inch',
    'in³': 'cubic inch',

    'gallon': 'gallon',
    'gallons': 'gallon',
    'gal': 'gallon',

    'micro': 'micrometre',
    'milli': 'millimetre',
    'centi': 'centimetre',
    'deci': 'decilitre',
    'kilo': 'kilogram',
}

quantity_unit_map = {
    'centimetre': ['width', 'depth', 'height'],
    'foot': ['width', 'depth', 'height'],
    'millimetre': ['width', 'depth', 'height'],
    'metre': ['width', 'depth', 'height'],
    'inch': ['width', 'depth', 'height'],
    'yard': ['width', 'depth', 'height'],

    'milligram': ['item_weight', 'maximum_weight_recommendation'],
    'kilogram': ['item_weight', 'maximum_weight_recommendation'],
    'microgram': ['item_weight', 'maximum_weight_recommendation'],
    'gram': ['item_weight', 'maximum_weight_recommendation'],
    'ounce': ['item_weight', 'maximum_weight_recommendation'],
    'ton': ['item_weight', 'maximum_weight_recommendation'],
    'pound': ['item_weight', 'maximum_weight_recommendation'],

    'millivolt': ['voltage'],
    'kilovolt': ['voltage'],
    'volt': ['voltage'],

    'kilowatt': ['wattage'],
    'watt': ['wattage'],

    'cubic foot': ['item_volume'],
    'microlitre': ['item_volume'],
    'cup': ['item_volume'],
    'fluid ounce': ['item_volume'],
    'centilitre': ['item_volume'],
    'imperial gallon': ['item_volume'],
    'pint': ['item_volume'],
    'decilitre': ['item_volume'],
    'litre': ['item_volume'],
    'millilitre': ['item_volume'],
    'quart': ['item_volume'],
    'cubic inch': ['item_volume'],
    'gallon': ['item_volume']
}

def quant_match(img_str, quantity='all'):
    num_one_or_two_words_regex = r'[\d]+(?:\.[\d]+)?\s[A-Za-z]+(?:\.\s?[A-Za-z]+)*(?:\s[A-Za-z]+)?'
    attached_unit_regex = r'[\d]+(?:\.[\d]+)?[A-Za-z]+'
    inches_or_feet_regex = r'[\d]+(?:\.[\d]+)?(?:\'|")'

    r1: list[str] = re.findall(num_one_or_two_words_regex, img_str)
    r2: list[str] = re.findall(attached_unit_regex, img_str)
    r3: list[str] = re.findall(inches_or_feet_regex, img_str)

    reg_match = r1 + r2 + r3
    
    transformed: list[str] = []

    for string in reg_match:
        string = string.lower()
        measurement = []
        for i in range(len(string)):
            if(not(string[i].isdigit() or string[i]==' ' or string[i]=='.') and string[i-1].isdigit()):
                measurement.append(' ')
                measurement.append(string[i])
            elif(string[i]=='.' and not(string[i-1].isdigit())):
                pass
            else:
                measurement.append(string[i])
        string = ''.join(measurement)
        transformed.append(string)

    all_measures: list[str] = []

    for string in transformed:
        temp = string.split(' ')
        num = str(float(temp[0]))
        unit = temp[1:]
        meas = [formal_unit[u] for u in unit if u in formal_unit.keys()]
        meas.insert(0, num)
        if len(meas)==1:
            pass
        elif(len(meas)==2 or len(meas)==3):
            all_measures.append(' '.join(meas))


    if len(all_measures)==0:
        return ''
    elif quantity=='all':
        return ', '.join(all_measures)
    else:
        filtered_measures = [measure for measure in all_measures if quantity in quantity_unit_map[measure[measure.find(' ') + 1:]]]
        if len(filtered_measures)==1:
            return filtered_measures[0]
        first = filtered_measures[0]
        measure = first[first.find(' ') + 1:]
        for ms in filtered_measures:
            if ms[ms.find(' ') + 1:]!=measure:
                break
        else:
            nums = [float(num[:num.find(' ')]) for num in filtered_measures]
            return (str(nums)+' '+measure)
        return ', '.join(filtered_measures)
