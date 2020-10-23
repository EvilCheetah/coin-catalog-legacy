
# General Information
You can access the following tables:

    - Family Related Tables:
        - Region
        - Country
        - Category
        - Collection
        - Coin Family
        - Coin Style

    - Author Related Tables:
        - Author (Designer) Name
        - Sculptor Name
        - Minted By

    - Characteristics Related Tables:
        - Material
        - Quality
        - Edge Style
        - Shape
        - Side

# Accessing Information
## Family Related Tables
### Region Table
#### Accessing All Items and Object Instance
To get a list of **all items** in the table, use given URL:  
`http://localhost:8000/region/`  

To get an **instance object**, use given URL:  
`http://localhost:8000/region/REGION_ID`,  
where REGION_ID is a specified _integer primary key_.  

#### Filtering Queryset
Filtering occurs on given URL:  
`http://localhost:8000/region/?`  

**Region Table** accepts given **parameters**:  
    - region

#### Parameter Description

**region**  
|||
|---|---|  
| Accepts        | **Region Name** or **Set of Names**(separated by comma) |  
| Parameter Type | STRING |  
| Search Field   | _region.name_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|  
| Query Sample   | region=Africa |

**Filtering Example:**  
`http://localhost:8000/region/?region=Europe,South America`  
Returns an object or set of objects, where  
    - Region Name is: `Europe` or `South America`.  

`http://localhost:8000/region/?region=Europe`  
Returns an object or set of objects, where   
    - Region Name is: `Europe`.

---

### Country Table
#### Accessing All Items and Object Instance
To get a list of **all items** in the table, use given URL:  
`http://localhost:8000/country/`  

To get an **instance object** , use given URL:  
`http://localhost:8000/country/COUNTRY_PK`,  
where COUNTRY_PK is a specified _integer primary key_.  

#### Filtering Queryset
Filtering occurs on given URL:  
`http://localhost:8000/country/?`  

**Country Table** accepts given **parameters**(can be combined):  
    - region  
    - country  

#### Parameter Description

**region**
|||
|---|---|  
| Accepts        | **Region ID** or **Set of Region IDs**(separated with comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _country.region_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | region=1,12 |

**country**
|||
|---|---|  
| Accepts        | **Country Name** or **Set of Names**(separated by comma) |  
| Parameter Type | STRING |  
| Search Field   | _country.name_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | country=UK |

**Filtering Example:**
`http://localhost:8000/country/?region=1,3&country=UK,France`  
Returns an object or set of objects, where  
    - Region ID is `1` or `3`  
    **AND**  
    - Country Name is `Europe` or `France`  

`http://localhost:8000/country/?country=Belarus`  
Returns an object or set of objects, where  
    - Country Name is `Belarus`

`http://localhost:8000/country/?region=1`  
Returns an object or set of objects, where  
    - Region ID is `1`

---

### Category Table
#### Accessing All Items and Object Instance
To get a list of **all items** in the table, use given URL:  
`http://localhost:8000/category/`  

To get an **instance object**, use given URL:  
`http://localhost:8000/category/CATEGORY_PK`,  
where CATEGORY_PK is a specified _integer primary key_.  

#### Filtering Queryset
Filtering occurs on given URL:  
`http://localhost:8000/category/?`  

**Category Table** accepts given **parameters**(can be combined):  
    - region  
    - country  
    - category

#### Parameter Description

**region**
|||
|---|---|  
| Accepts        | **Region ID** or **Set of IDs**(separated with comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _category.country.region_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | region=14 |

**country**
|||
|---|---|  
| Accepts        | **Country ID** or **Set of IDs**(separated by comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _category.country_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | country=12,13 |

**category**
|||
|---|---|  
| Accepts        | **Category Name** or **Set of Names**(separated by comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _category.name_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | category=History,Gods |

**Filtering Example:**
`http://localhost:8000/category/?region=2,3&country=France,Mexico`  
Returns an object or set of objects, where  
    - Region ID is `2` or `3`  
    **AND**  
    - Country Name is `France` or `Mexico`

---

### Collection Table
#### Accessing All Items and Object Instance
To get a list of **all items** in the table, use given URL:  
`http://localhost:8000/collection/`  

To get an **instance object**, use given URL:  
`http://localhost:8000/collection/COLLECTION_PK`,  
where COLLECTION_PK is a specified _integer primary key_.  

#### Filtering Queryset
Filtering occurs on given URL:  
`http://localhost:8000/collection/?`  

**Collection Table** accepts given **parameters**(can be combined):  
    - region  
    - country  
    - category  
    - collection

#### Parameter Description

**region**
|||
|---|---|  
| Accepts        | **Region ID** or **Set of IDs**(separated with comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _collection.category.country.region_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | region=7 |

**country**
|||
|---|---|  
| Accepts        | **Country ID** or **Set of IDs**(separated by comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _collection.category.country_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | country=1,5 |

**category**
|||
|---|---|  
| Accepts        | **Category ID** or **Set of IDs**(separated by comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _collection.category_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | category=13 |

**collection**
|||
|---|---|  
| Accepts        | **Collection Name** or **Set of Names**(separated by comma) |  
| Parameter Type | STRING |  
| Search Field   | _collection.category.name_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | collection=2,5 |

**Filtering Example:**
`http://localhost:8000/collection/?region=2,3&country=France,Mexico`  
Returns an object or set of objects, where  
    - Region ID is `2` or `3`  
    **AND**  
    - Country Name is `France` or `Mexico`

---


### Coin Family Table
#### Accessing All Items and Object Instance
To get a list of **all items** in the table, use given URL:  
`http://localhost:8000/coin_family/`  

To get an **instance object**, use given URL:  
`http://localhost:8000/coin_family/COIN_FAMILY_PK`,  
where COIN_FAMILY_PK is a specified _integer primary key_.  

#### Filtering Queryset
Filtering occurs on given URL:  
`http://localhost:8000/coin_family/?`  

**Coin Family Table** accepts given **parameters**(can be combined):  
    - region  
    - country  
    - category  
    - collection  
    - minted_by

#### Parameter Description

**region**
|||
|---|---|  
| Accepts        | **Region ID** or **Set of IDs**(separated with comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _coin_family.collection.category.country.region_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | region=15 |

**country**
|||
|---|---|  
| Accepts        | **Country ID** or **Set of IDs**(separated by comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _coin_family.collection.category.country_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | country=7 |

**category**
|||
|---|---|  
| Accepts        | **Category ID** or **Set of IDs**(separated by comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _coin_family.collection.category_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | category=11 |

**collection**
|||
|---|---|  
| Accepts        | **Collection ID** or **Set of IDs**(separated by comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _coin_family.collection_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | collection=8 |

**minted_by**
|||
|---|---|  
| Accepts        | **Minted By ID** or **Set of IDs**(separated by comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _coin_family.minted_by_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | minted_by=1,2 |

**Filtering Example:**
`http://localhost:8000/coin_family/?collection=9,13`  
Returns an object or set of objects, where  
    - Region ID is `9` or `13`  

`http://localhost:8000/coin_family/?country=12,32`  
Returns an object or set of objects, where  
    - Country ID is `12` or `32`  

`http://localhost:8000/coin_family/?region=2&minted_by=1,15`  
Returns an object or set of objects, where  
    - Region ID is `2` or `3`  
    **AND**  
    - Minted By ID is `1` or `15`

---

### Coin Style Table
#### Accessing All Items and Object Instance
To get a list of **all items** in the table, use given URL:  
`http://localhost:8000/coin_style/`  

To get an **instance object**, use given URL:  
`http://localhost:8000/coin_style/COIN_STYLE_PK`,  
where COIN_STYLE_PK is a specified _integer primary key_.  

#### Filtering Queryset
Filtering occurs on given URL:  
`http://localhost:8000/coin_style/?`  

**High Priority Filter**(cannot be combined):  
    - KM Number  
        **If found returns a queryset without looking at  
        other parameters**  

**Coin Style Table** accepts given **parameters**(can be combined - order doesn't matter):  
    - region  
    - country  
    - category  
    - collection  
    - coin_family  
    - minted_by  
    - year  
    - shape  
    - quality  
    - edge  
    - material  
    - standard  
    - denomination  
    - mintage  
    - weight  
    - length  
    - width  
    - thickness  

#### Parameter Description

**Range Items May be given in different formats**  
_Example on Length_:  
    - `length=19-35`: returns coins which length lies in range [19; 35]  
    - `length=-85`: returns coins which length is less than or equal to `85`  
    - `length=13-`: returns coins which length is greater than or equal to `13`  
    - `length=-`: avoids filtering and returning all objects  

**region**
|||
|---|---|  
| Accepts        | **Region ID** or **Set of IDs**(separated with comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _coin_style.coin_family.collection.category.country.region_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | region=1,3 |

**country**
|||
|---|---|  
| Accepts        | **Country ID** or **Set of IDs**(separated by comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _coin_style.coin_family.collection.category.country_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | country=1,9 |

**category**
|||
|---|---|  
| Accepts        | **Category ID** or **Set of IDs**(separated by comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _coin_style.coin_family.collection.category_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | category=1,7 |

**collection**
|||
|---|---|  
| Accepts        | **Collection ID** or **Set of IDs**(separated by comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _coin_style.coin_family.collection_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | collection=12,15 |

**coin_family**
|||
|---|---|  
| Accepts        | **Coin Family ID** or **Set of IDs**(separated by comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _coin_style.coin_family.collection_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | coin_family=8 |

**minted_by**
|||
|---|---|  
| Accepts        | **Minted By ID** or **Set of IDs**(separated by comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _coin_style.coin_family.minted_by_id_ |  
| Filter Lookup  | _Co |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | minted_by=1,2 |

**year**
|||
|---|---|  
| Accepts        | **Year Range**(separated by hyphen) |  
| Parameter Type | INTEGER |  
| Search Field   | _coin_style.year_ |  
| Filter Lookup  | _Range_ |  
| Returns        | Filtered Queryset, which items fall into specified range|
| Query Sample   | year=1999-2000 |

**shape**
|||
|---|---|  
| Accepts        | **Shape ID** or **Set of IDs**(separated by comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _coin_style.shape_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | shape=1,2,5 |

**quality**
|||
|---|---|  
| Accepts        | **Quality ID** or **Set of IDs**(separated by comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _coin_style.quality_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | quality=1,5,7 |

**edge**
|||
|---|---|  
| Accepts        | **Edge ID** or **Set of IDs**(separated by comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _coin_style.edge_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | edge=1,2,3 |

**material**
|||
|---|---|  
| Accepts        | **Material ID** or **Set of IDs**(separated by comma) |  
| Parameter Type | INTEGER |  
| Search Field   | _coin_style.material_id_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | material=1,2,4 |

**standard**
|||
|---|---|  
| Accepts        | **Standard Range**(separated by hyphen) |  
| Parameter Type | FLOAT |  
| Search Field   | _coin_style.standard_ |  
| Filter Lookup  | _Range_ |  
| Returns        | Filtered Queryset, which items fall into specified range|
| Query Sample   | standard=925-999 |

**denomination**
|||
|---|---|  
| Accepts        | **Denomination** or **Set of Denominations**(separated by comma) |  
| Parameter Type | STRING |  
| Search Field   | _coin_style_.denomination_ |  
| Filter Lookup  | _Exact_ |  
| Returns        | Filtered Queryset, with exact match|
| Query Sample   | denomination=20 BYR,30 EUR |

**mintage**
|||
|---|---|  
| Accepts        | **Mintage Range**(separated by hyphen) |  
| Parameter Type | INTEGER |  
| Search Field   | _coin_style.mintage_ |  
| Filter Lookup  | _Range_ |  
| Returns        | Filtered Queryset, which items fall into specified range|
| Query Sample   | mintage=300-500 |

**weight**
|||
|---|---|  
| Accepts        | **Weight Range**(separated by hyphen) |  
| Parameter Type | FLOAT |  
| Search Field   | _coin_style.weight_ |  
| Filter Lookup  | _Range_ |  
| Returns        | Filtered Queryset, which items fall into specified range|
| Query Sample   | weight=33.3-45.0 |

**length**
|||
|---|---|  
| Accepts        | **Length Range**(separated by hyphen) |  
| Parameter Type | FLOAT |  
| Search Field   | _coin_style.length_ |  
| Filter Lookup  | _Range_ |  
| Returns        | Filtered Queryset, which items fall into specified range|
| Query Sample   | length=18.0-34.0 |

**width**
|||
|---|---|  
| Accepts        | **Width Range**(separated by hyphen) |  
| Parameter Type | FLOAT |  
| Search Field   | _coin_style.width_ |  
| Filter Lookup  | _Range_ |  
| Returns        | Filtered Queryset, which items fall into specified range|
| Query Sample   | width=10.0-50.0 |

**thickness**
|||
|---|---|  
| Accepts        | **thickness Range**(separated by hyphen) |  
| Parameter Type | FLOAT |  
| Search Field   | _coin_style.thickness_ |  
| Filter Lookup  | _Range_ |  
| Returns        | Filtered Queryset, which items fall into specified range|
| Query Sample   | thickness=5.00-10.0 |

**Filtering Example:**
`http://localhost:8000/coin_family/?country=1,3&year=1950-2011&material=1,2&length=10.0-39.0`  
Returns an object or set of objects, where  
    - Country ID is `1` or `3`  
    **AND**  
    - Year Range is `1950 <= Year <= 2011`  
    **AND**  
    - Material ID is `1` or `2`  
    **AND**  
    - Length Range is `10.0 <= Length <= 39.0`  

---

### Author Table
#### Accessing All Items and Object Instance
To get a list of **all items** in the table, use given URL:  
`http://localhost:8000/author_name/`  

To get an **instance object**, use given URL:  
`http://localhost:8000/author_name/AUTHOR_PK`,  
where AUTHOR_PK is a specified _integer primary key_.  

**Author Table Doesn't Support Filtering**

---

### Sculptor Table
#### Accessing All Items and Object Instance
To get a list of **all items** in the table, use given URL:  
`http://localhost:8000/sculptor_name/`  

To get an **instance object**, use given URL:  
`http://localhost:8000/sculptor_name/SCULPTOR_PK`,  
where SCULPTOR_PK is a specified _integer primary key_.  

**Sculptor Table Doesn't Support Filtering**

---

### Minted By Table
#### Accessing All Items and Object Instance
To get a list of **all items** in the table, use given URL:  
`http://localhost:8000/minted_by/`  

To get an **instance object**, use given URL:  
`http://localhost:8000/minted_by/MINTED_BY_PK`,  
where MINTED_BY_PK is a specified _integer primary key_.  

**Minted By Table Doesn't Support Filtering**

---

### Material Table
#### Accessing All Items and Object Instance
To get a list of **all items** in the table, use given URL:  
`http://localhost:8000/material/`  

To get an **instance object**, use given URL:  
`http://localhost:8000/material/MATERIAL_PK`,  
where MATERIAL_PK is a specified _integer primary key_.  

**Material Table Doesn't Support Filtering**

---

### Quality Table
#### Accessing All Items and Object Instance
To get a list of **all items** in the table, use given URL:  
`http://localhost:8000/quality/`  

To get an **instance object**, use given URL:  
`http://localhost:8000/quality/QUALITY_PK`,  
where QUALITY_PK is a specified _integer primary key_.  

**Quality Table Doesn't Support Filtering**

---

### Edge Style Table
#### Accessing All Items and Object Instance
To get a list of **all items** in the table, use given URL:  
`http://localhost:8000/edge/`  

To get an **instance object**, use given URL:  
`http://localhost:8000/edge/EDGE_STYLE_PK`,  
where EDGE_STYLE_PK is a specified _integer primary key_.  

**Edge Style Table Doesn't Support Filtering**

---

### Shape Table
#### Accessing All Items and Object Instance
To get a list of **all items** in the table, use given URL:  
`http://localhost:8000/shape/`  

To get an **instance object**, use given URL:  
`http://localhost:8000/shape/SHAPE_PK`,  
where SHAPE_PK is a specified _integer primary key_.  

**Shape Table Doesn't Support Filtering**

---

### Side Table
#### Accessing All Items and Object Instance
To get a list of **all items** in the table, use given URL:  
`http://localhost:8000/side_of_coin/`  

To get an **instance object**, use given URL:  
`http://localhost:8000/side_of_coin/SIDE_PK`,  
where SIDE_PK is a specified _integer primary key_.  

**Side Table Doesn't Support Filtering**
