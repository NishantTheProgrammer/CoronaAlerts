def get():
    import COVID19Py
    covid19 = COVID19Py.COVID19()
    locations = covid19.getLocations()
    ids = [
        0, #Afghanistan
        1, #Albania
        2, #Algeria
        3, #Andorra
        4, #Angola
        5, #Antigua and Barbuda
        6, #Argentina
        7, #Armenia
        9, #Australia
        16, #Austria
        17, #Azerbaijan
        18, #Bahamas
        19, #Bahrain
        20, #Bangladesh
        21, #Barbados
        22, #Belarus
        23, #Belgium
        24, #Benin
        25, #Bhutan
        26, #Bolivia
        27, #Bosnia and Herzegovina
        28, #Brazil
        29, #Brunei
        30, #Bulgaria
        31, #Burkina Faso
        32, #Cabo Verde
        33, #Cambodia
        34, #Cameroon
        44, #Canada
        46, #Central African Republic
        47, #Chad
        48, #Chile
        62, #China
        82, #Colombia
        83, #Congo (Brazzaville)
        85, #Costa Rica
        86, #Cote d'Ivoire
        87, #Croatia
        88, #Diamond Princess
        89, #Cuba
        90, #Cyprus
        91, #Czechia
        94, #Denmark
        95, #Djibouti
        96, #Dominican Republic
        97, #Ecuador
        98, #Egypt
        99, #El Salvador
        100, #Equatorial Guinea
        101, #Eritrea
        102, #Estonia
        103, #Eswatini
        104, #Ethiopia
        105, #Fiji
        106, #Finland
        116, #France
        117, #Gabon
        118, #Gambia
        119, #Georgia
        120, #Germany
        121, #Ghana
        122, #Greece
        123, #Guatemala
        124, #Guinea
        125, #Guyana
        126, #Haiti
        127, #Holy See
        128, #Honduras
        129, #Hungary
        130, #Iceland
        131, #India
        132, #Indonesia
        133, #Iran
        134, #Iraq
        135, #Ireland
        136, #Israel
        137, #Italy
        138, #Jamaica
        139, #Japan
        140, #Jordan
        141, #Kazakhstan
        142, #Kenya
        143, #Korea, South
        144, #Kuwait
        145, #Kyrgyzstan
        146, #Latvia
        147, #Lebanon
        148, #Liberia
        149, #Liechtenstein
        150, #Lithuania
        151, #Luxembourg
        152, #Madagascar
        153, #Malaysia
        154, #Maldives
        155, #Malta
        156, #Mauritania
        157, #Mauritius
        158, #Mexico
        159, #Moldova
        160, #Monaco
        161, #Mongolia
        162, #Montenegro
        163, #Morocco
        164, #Namibia
        165, #Nepal
        169, #Netherlands
        170, #New Zealand
        171, #Nicaragua
        172, #Niger
        173, #Nigeria
        174, #North Macedonia
        175, #Norway
        176, #Oman
        177, #Pakistan
        178, #Panama
        179, #Papua New Guinea
        180, #Paraguay
        181, #Peru
        182, #Philippines
        183, #Poland
        184, #Portugal
        185, #Qatar
        186, #Romania
        187, #Russia
        188, #Rwanda
        189, #Saint Lucia
        190, #Saint Vincent and the Grenadines
        191, #San Marino
        192, #Saudi Arabia
        193, #Senegal
        194, #Serbia
        195, #Seychelles
        196, #Singapore
        197, #Slovakia
        198, #Slovenia
        199, #Somalia
        200, #South Africa
        201, #Spain
        202, #Sri Lanka
        203, #Sudan
        204, #Suriname
        205, #Sweden
        206, #Switzerland
        207, #Taiwan*
        208, #Tanzania
        209, #Thailand
        210, #Togo
        211, #Trinidad and Tobago
        212, #Tunisia
        213, #Turkey
        214, #Uganda
        215, #Ukraine
        216, #United Arab Emirates
        224, #Uruguay
        225, #US
        226, #Uzbekistan
        227, #Venezuela
        228, #Vietnam
        229, #Zambia
        230, #Zimbabwe
        232, #Dominica
        233, #Grenada
        234, #Mozambique
        235, #Syria
        236, #Timor-Leste
        237, #Belize
        239, #Laos
        240, #Libya
        241, #West Bank and Gaza
        242, #Guinea-Bissau
        243, #Mali
        244, #Saint Kitts and Nevis
        247, #Kosovo
        248, #Burma
        252, #MS Zaandam
        253, #Botswana
        254, #Burundi
        255, #Sierra Leone
        257 #Malawi
    ]





    data = []
    for i in range(len(locations)):
        id = locations[i]['id']
        if(id in ids):
            country = locations[i]['country']
            confirmed = locations[i]['latest']['confirmed']
            deaths = locations[i]['latest']['deaths']

            data.append((id, country, confirmed, deaths))

    return(data)
    
