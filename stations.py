line_colors = {
    "Victoria": "#0098D4",
    "Central": "#E32017",
    "Metropolitan": "#751056",
    "Bakerloo": "#B36305",
    "Circle": "#FFD300",
    "Hammersmith and City": "#F3A9BB",
    "Jubilee": "#6A7278",
    "Northern": "#000000",
    "Waterloo and City": "#76D0BD",
    "District": "#00782A",
    "Piccadilly": "#003688",
    "Tramlink": "#1EFF00",
    "Overground": "#EE7C0E",
    "Elizabeth Line": "#B300FF",
    "DLR": "#3CDCEB",
    "Walking": "#555555",
    "Other": "#999999"
}

line_station_orders = {
    "Victoria": 
    [
            "Brixton",
            "Stockwell",
            "Vauxhall",
            "Pimlico",
            "Victoria",
            "Green Park",
            "Oxford Circus",
            "Warren Street",
            "Euston",
            "King's Cross St. Pancras",
            "Highbury & Islington",
            "Finsbury Park",
            "Seven Sisters",
            "Tottenham Hale",
            "Blackhorse Road",
            "Walthamstow Central"
        ],

    "Central": 
    [
        [
            "Ealing Broadway", 
            "West Acton", 
            "North Acton"
        ],

        [
            "West Ruislip", 
            "Ruislip Gardens", 
            "South Ruislip", 
            "Northolt", 
            "Greenford",
            "Perivale", 
            "Hanger Lane",
            "North Acton", 
            "East Acton", 
            "White City", 
            "Shepherd's Bush", 
            "Holland Park",
            "Notting Hill Gate",
            "Queensway",
            "Lancaster Gate",
            "Marble Arch",
            "Bond Street",
            "Oxford Circus",
            "Tottenham Court Road",
            "Holborn",
            "Chancery Lane",
            "St. Paul's",
            "Bank",
            "Liverpool Street",
            "Bethnal Green", 
            "Mile End", 
            "Stratford", 
            "Leyton",
            "Leytonstone",
            "Snaresbrook", 
            "South Woodford",
            "Woodford",
            "Buckhurst Hill",
            "Loughton",
            "Debden",
            "Theydon Bois",
            "Epping"
        ],

        [
            "Leytonstone", 
            "Wanstead", 
            "Redbridge", 
            "Gants Hill", 
            "Newbury Park",
            "Barkingside", 
            "Fairlop", 
            "Hainault",
            "Grange Hill",
            "Chigwell",
            "Roding Valley",
            "Woodford",
        ],
    ],

    "Piccadilly": 
    [

        [
            "Uxbridge", 
            "Hillingdon", 
            "Ickenham", 
            "Ruislip", 
            "Ruislip Manor",
            "Eastcote", 
            "Rayners Lane", 
            "South Harrow", 
            "Sudbury Hill",
            "Sudbury Town", 
            "Alperton", 
            "Park Royal", 
            "North Ealing",
            "Ealing Common", 
            "Acton Town"
        ],

        [
            "Hatton Cross",
            "Heathrow Terminal 4",
            "Heathrow Terminals 1-2-3"
        ],

        [
            "Heathrow Terminal 5", 
            "Heathrow Terminals 1-2-3", 
            "Hatton Cross", 
            "Hounslow West", 
            "Hounslow Central", 
            "Hounslow East",
            "Osterley", 
            "Boston Manor", 
            "Northfields", 
            "South Ealing",
            "Acton Town",
            "Turnham Green",
            "Hammersmith (Dist&Picc Line)", 
            "Barons Court", 
            "Earl's Court",
            "Gloucester Road", 
            "South Kensington", 
            "Knightsbridge", 
            "Hyde Park Corner",
            "Green Park", 
            "Piccadilly Circus", 
            "Leicester Square", 
            "Covent Garden",
            "Holborn", 
            "Russell Square", 
            "King's Cross St. Pancras", 
            "Caledonian Road",
            "Holloway Road", 
            "Arsenal", 
            "Finsbury Park", 
            "Manor House",
            "Turnpike Lane", 
            "Wood Green", 
            "Bounds Green", 
            "Arnos Grove",
            "Southgate", 
            "Oakwood", 
            "Cockfosters"
        ]
    ],

    "Circle": 
    [
        "Hammersmith (H&C Line)",
        "Goldhawk Road",
        "Shepherd's Bush Market",
        "Wood Lane",
        "Latimer Road",
        "Ladbroke Grove",
        "Westbourne Park",
        "Royal Oak",
        "Paddington (H&C Line)",
        "Edgware Road (Circle Line)",
        "Baker Street",
        "Great Portland Street",
        "Euston Square",
        "King's Cross St. Pancras",
        "Farringdon",
        "Barbican",
        "Moorgate",
        "Liverpool Street",
        "Aldgate",
        "Tower Hill",
        "Monument",
        "Cannon Street",
        "Mansion House",
        "Blackfriars",
        "Temple",
        "Embankment",
        "Westminster",
        "St. James's Park",
        "Victoria",
        "Sloane Square",
        "South Kensington",
        "Gloucester Road",
        "High Street Kensington",
        "Notting Hill Gate",
        "Bayswater",
        "Paddington",
        "Edgware Road (Circle Line)"
    ],

    "District": 
    [
        [
            "Ealing Broadway",
            "Ealing Common",
            "Acton Town",
            "Chiswick Park",
            "Turnham Green",
            "Stamford Brook",
            "Ravenscourt Park",
            "Hammersmith (Dist&Picc Line)",
            "Barons Court",
            "West Kensington",
            "Earl's Court",
            "Gloucester Road",
            "South Kensington",
            "Sloane Square",
            "Victoria",
            "St. James's Park",
            "Westminster",
            "Embankment",
            "Temple",
            "Blackfriars",
            "Mansion House",
            "Cannon Street",
            "Monument",
            "Tower Hill",
            "Aldgate East",
            "Whitechapel",
            "Stepney Green",
            "Mile End",
            "Bow Road",
            "Bromley-by-Bow",
            "West Ham",
            "Plaistow",
            "Upton Park",
            "East Ham",
            "Barking",
            "Upney",
            "Becontree",
            "Dagenham Heathway",
            "Dagenham East",
            "Elm Park",
            "Hornchurch",
            "Upminster Bridge",
            "Upminster",
        ],

        [
            "Earl's Court",
            "West Brompton",
            "Fulham Broadway",
            "Parsons Green",
            "Putney Bridge",
            "East Putney",
            "Southfields",
            "Wimbledon Park",
            "Wimbledon"
        ],

        [
            "Earl's Court",
            "High Street Kensington",
            "Notting Hill Gate",
            "Bayswater",
            "Paddington",
            "Edgware Road (Circle Line)",
        ],

        [
            "Earl's Court",
            "Kensington Olympia"
        ],

        [
            "Turnham Green",
            "Chiswick Park",
            "Gunnersbury",
            "Kew Gardens",
            "Richmond",
        ],


    ],

    "Bakerloo": 
    [
        "Harrow & Wealdstone",
        "Kenton",
        "South Kenton",
        "North Wembley",
        "Wembley Central",
        "Stonebridge Park",
        "Harlesden",
        "Willesden Junction",
        "Kensal Green",
        "Queen's Park",
        "Kilburn Park",
        "Maida Vale",
        "Warwick Avenue",
        "Paddington", 
        "Edgware Road (Bakerloo)", 
        "Marylebone", 
        "Baker Street", 
        "Regent's Park", 
        "Oxford Circus", 
        "Piccadilly Circus", 
        "Charing Cross", 
        "Embankment", 
        "Waterloo", 
        "Lambeth North", 
        "Elephant & Castle"
    ],

    "Waterloo and City": 
    [
        "Waterloo",
        "Bank"
    ],

    "Jubilee": 
    [
        "Stanmore",
        "Canons Park",
        "Queensbury",
        "Kingsbury",
        "Wembley Park",
        "Neasden",
        "Dollis Hill",
        "Willesden Green",
        "Kilburn",
        "West Hampstead",
        "Finchley Road",
        "Swiss Cottage",
        "St. John's Wood",
        "Baker Street",
        "Bond Street",
        "Green Park",
        "Westminster",
        "Waterloo",
        "Southwark",
        "London Bridge",
        "Bermondsey",
        "Canada Water",
        "Canary Wharf",
        "North Greenwich",
        "Canning Town",
        "West Ham",
        "Stratford"
    ],

    "Metropolitan":    
    [
        [
            "Aldgate", 
            "Liverpool Street", 
            "Moorgate", 
            "Barbican", 
            "Farringdon", 
            "King's Cross St. Pancras", 
            "Euston Square", 
            "Great Portland Street", 
            "Baker Street",
            "Finchley Road",
            "Wembley Park",
            "Preston Road",
            "Northwick Park",
            "Harrow-on-the-Hill",
            "North Harrow",
            "Pinner",
            "Northwood Hills",
            "Northwood",
            "Moor Park",
            "Rickmansworth",
            "Chorleywood",
            "Chalfont & Latimer",
            "Amersham",
        ],

        [
            "Chalfont & Latimer",
            "Chesham",
        ],

        [
            "Harrow-on-the-Hill",
            "West Harrow",
            "Rayners Lane",
            "Eastcote",
            "Ruislip Manor",
            "Ruislip",
            "Ickenham",
            "Hillingdon",
            "Uxbridge",
        ],

        [
            "Moor Park",
            "Croxley",
            "Watford"
        ],
    ],   

    "Hammersmith and City": 
    [
        "Hammersmith (H&C Line)",
        "Goldhawk Road",
        "Shepherd's Bush Market",
        "Wood Lane",
        "Latimer Road",
        "Ladbroke Grove",
        "Westbourne Park",
        "Royal Oak",
        "Paddington (H&C Line)",
        "Edgware Road (Circle Line)",
        "Baker Street",
        "Great Portland Street",
        "Euston Square",
        "King's Cross St. Pancras",
        "Farringdon",
        "Barbican",
        "Moorgate",
        "Liverpool Street",
        "Aldgate East",
        "Whitechapel",
        "Stepney Green",
        "Mile End",
        "Bow Road",
        "Bromley-by-Bow",
        "West Ham",
        "Plaistow",
        "Upton Park",
        "East Ham",
        "Barking",
    ],

    "Northern": 
    [

        [
            "Morden",
            "South Wimbledon",
            "Colliers Wood",
            "Tooting Broadway",
            "Tooting Bec",
            "Balham",
            "Clapham South",
            "Clapham Common",
            "Clapham North",
            "Stockwell",
            "Oval",
            "Kennington",
            "Borough",
            "London Bridge",
            "Bank",
            "Moorgate",
            "Old Street",
            "Angel",
            "King's Cross St. Pancras",
            "Euston",
            "Mornington Crescent",
            "Camden Town",
            "Kentish Town",
            "Tufnell Park",
            "Archway",
            "Highgate",
            "East Finchley",
            "Finchley Central",
            "West Finchley",
            "Woodside Park",
            "Totteridge & Whetstone",
            "High Barnet"
        ],

        [
            "Finchley Central",
            "Mill Hill East"
        ],

        [
            "Kennington",
            "Waterloo",
            "Embankment",
            "Charing Cross",
            "Leicester Square",
            "Tottenham Court Road",
            "Goodge Street",
            "Warren Street",
            "Euston",
            "Camden Town",
            "Chalk Farm",
            "Belsize Park",
            "Hampstead",
            "Golders Green",
            "Brent Cross",
            "Hendon Central",
            "Colindale",
            "Burnt Oak",
            "Edgware"
        ],
    ],

    "Tramlink": 
    [

        [
            "Beckenham Junction (Tramlink)",
            "Beckenham Road",
            "Avenue Road",
            "Birkbeck (Tramlink)",
            "Harrington Road",
            "Arena",
            "Woodside",
            "Blackhorse Lane",
            "Addiscombe",
            "Sandilands",
            "Lebanon Road",
            "East Croydon (Tramlink)",
            "Wellesley Road",
            "West Croydon",
            "Centrale",
            "Reeves Corner",
            "Wandle Park",
            "Waddon Marsh",
            "Ampere Way",
            "Therapia Lane",
            "Beddington Lane",
            "Mitcham Junction (Tramlink)",
            "Mitcham",
            "Belgrave Walk",
            "Phipps Bridge",
            "Morden Road",
            "Merton Park",
            "Dundonald Road",
            "Wimbledon (Tramlink)"
        ],

        [
            "New Addington",
            "King Henry's Drive",
            "Fieldway",
            "Addington Village",
            "Gravel Hill",
            "Coombe Lane",
            "Lloyd Park",
            "Sandilands",
        ],

        [
            "Elmers End (Tramlink)",
            "Arena",
        ],

        [
            "East Croydon (Tramlink)",
            "George Street",
            "Church Street",
            "Centrale",
        ]

    ],

    "Overground":
    [
        [
            "Upminster",
            "Emerson Park",
            "Romford"
        ],

        [
            "Richmond",
            "Kew Gardens",
            "Gunnersbury",
            "South Acton",
            "Acton Central",
            "Willesden Junction (Overground)",
            "Kensal Rise",
            "Brondesbury Park",
            "Brondesbury",
            "West Hampstead",
            "Finchley Road & Frognal",
            "Hampstead Heath",
            "Gospel Oak",
            "Kentish Town West",
            "Camden Road",
            "Caledonian Road & Barnsbury",
            "Highbury & Islington",
            "Canonbury",
            "Dalston Kingsland",
            "Hackney Central",
            "Homerton",
            "Hackney Wick",
            "Stratford"
        ],

        [
            "Clapham Junction",
            "Imperial Wharf",
            "West Brompton",
            "Kensington (Olympia)",
            "Shepherd's Bush (Overground)",
            "Willesden Junction (Overground)"
        ],

        [
            "Clapham Junction",
            "Wandsworth Road",
            "Clapham High Street",
            "Denmark Hill",
            "Peckham Rye",
            "Queens Road Peckham",
            "Surrey Quays",
            "Canada Water",
            "Rotherhithe",
            "Wapping",
            "Shadwell",
            "Whitechapel",
            "Shoreditch High Street",
            "Hoxton",
            "Haggerston",
            "Dalston Junction",
            "Canonbury",
            "Highbury & Islington"
        ],

        [
            "Surrey Quays",
            "New Cross"
        ],

        [
            "Sydenham",
            "Crystal Palace"
        ],

        [
            "Surrey Quays",
            "New Cross Gate",
            "Brockley",
            "Honor Oak Park",
            "Forest Hill",
            "Sydenham",
            "Penge West",
            "Anerley",
            "Norwood Junction",
            "West Croydon"
        ],

        [
            "Gospel Oak",
            "Upper Holloway",
            "Crouch Hill",
            "Harringay Green Lanes",
            "South Tottenham",
            "Blackhorse Road",
            "Walthamstow Queens Road",
            "Leyton Midland Road",
            "Leytonstone High Road",
            "Wanstead Park",
            "Woodgrange Park",
            "Barking",
        ],

        [
            "Euston",
            "South Hampstead",
            "Kilburn High Road",
            "Queen's Park",
            "Kensal Green",
            "Willesden Junction",
            "Harlesden",
            "Stonebridge Park",
            "Wembley Central",
            "North Wembley",
            "South Kenton",
            "Kenton",
            "Harrow & Wealdstone",
            "Headstone Lane",
            "Hatch End",
            "Carpenders Park",
            "Bushey",
            "Watford High Street",
            "Watford Junction"
        ],
    
        [
            "Liverpool Street",
            "Bethnal Green",
            "Cambridge Heath",
            "London Fields",
            "Hackney Downs",
            "Rectory Road",
            "Stoke Newington",
            "Stamford Hill",
            "Seven Sisters",
            "Bruce Grove",  
            "White Hart Lane",
            "Silver Street",
            "Edmondton Green",
            "Southbury",
            "Turkey Street",
            "Theobalds Grove",
            "Cheshunt"
        ],

        [
            "Enfield Town",
            "Bush Hill Park",
            "Edmondton Green"
        ],

        [
            "Bethnal Green",
            "Hackney Downs",
            "Clapton",
            "St James Street",
            "Walthamstow Central",
            "Wood Street",
            "Highams Park",
            "Chingford"
        ],
    ],

    "Elizabeth Line": 
    [

        [
            "West Drayton",
            "Hayes & Harlington",
        ],

        [
            "Heathrow Terminal 4",
            "Heathrow Terminals 2 & 3"
        ],
    
        [
            "Heathrow Terminal 5",
            "Heathrow Terminals 2 & 3",
            "Hayes & Harlington",
            "Southall",
            "Hanwell",
            "West Ealing",
            "Ealing Broadway",
            "Acton Main Line",
            "Paddington",
            "Bond Street",
            "Tottenham Court Road",
            "Farringdon",
            "Liverpool Street",
            "Whitechapel",
            "Canary Wharf",
            "Custom House",
            "Woolwich",
            "Abbey Wood"
        ],

        [
            "Liverpool Street",
            "Stratford",
            "Maryland",
            "Forest Gate",
            "Manor Park",
            "Ilford",
            "Seven Kings",
            "Goodmayes",
            "Chadwell Heath",
            "Romford",
            "Gidea Park",
            "Harold Wood",
            "Brentwood",
            "Shenfield"        
        ],
    ],

    "DLR": 
    [
        [
            "LEWISHAM (DLR)",
            "ELVERSON ROAD (DLR)",
            "DEPTFORD BRIDGE (DLR)",
            "GREENWICH (DLR)",
            "CUTTY SARK (DLR)",
            "ISLAND GARDENS (DLR)",
            "MUDCHUTE (DLR)",
            "CROSSHARBOUR (DLR)",
            "SOUTH QUAY (DLR)",
            "HERON QUAYS (DLR)",
            "CANARY WHARF (DLR)",
            "WEST INDIA QUAY (DLR)",
            "WESTFERRY (DLR)",
            "POPLAR (DLR)",
            "ALL SAINTS (DLR)",
            "LANGDON PARK (DLR)",
            "DEVONS ROAD (DLR)",
            "BOW CHURCH (DLR)",
            "PUDDING MILL LANE (DLR)",
            "STRATFORD (DLR)"
        ],

        [
            "STRATFORD INTERNATIONAL (DLR)",
            "STRATFORD (DLR)",
            "STRATFORD HIGH STREET (DLR)",
            "ABBEY ROAD (DLR)",
            "WEST HAM (DLR)",
            "STAR LANE (DLR)",
            "CANNING TOWN (DLR)",
            "WEST SILVERTOWN (DLR)",
            "PONTOON DOCK (DLR)",
            "LONDON CITY AIRPORT (DLR)",
            "KING GEORGE V (DLR)",
            "WOOLWICH ARSENAL (DLR)"
        ],

        [
            "TOWER GATEWAY (DLR)",
            "SHADWELL (DLR)",
            "LIMEHOUSE (DLR)",
            "WESTFERRY (DLR)",
            "POPLAR (DLR)",
            "BLACKWALL (DLR)",
            "EAST INDIA (DLR)",
            "CANNING TOWN (DLR)",
            "ROYAL VICTORIA (DLR)",
            "CUSTOM HOUSE (DLR)",
            "PRINCE REGENT (DLR)",
            "ROYAL ALBERT (DLR)",
            "BECKTON PARK (DLR)",
            "CYPRUS (DLR)",
            "GALLIONS REACH (DLR)",
            "BECKTON (DLR)"
        ],

        [
            "BANK (DLR)",
            "SHADWELL (DLR)"
        ],

        [
            "WESTFERRY (DLR)",
            "WEST INDIA QUAY (DLR)"
        ],
    ],

    "Walking":
    [
        [
            "Wimbledon",
            "Wimbledon (Tramlink)"
        ],

        [
            "Shepherd's Bush",
            "Shepherd's Bush (Overground)"
        ],

        [
            "Willesden Junction",
            "Willesden Junction (Overground)"
        ],

        [
            "White City",
            "Wood Lane"
        ],   

        [
            "South Wimbledon",
            "Morden Road"
        ],

        [
            "Heathrow Terminals 2 & 3",
            "Heathrow Terminals 1-2-3"
        ],

        [
            "Hackney Downs",
            "Hackney Central"
        ],
    ]

}
