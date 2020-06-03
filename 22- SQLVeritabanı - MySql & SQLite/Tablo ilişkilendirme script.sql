alter table products
add CONSTRAINT fk_cagetories_products
FOREIGN KEY (Categoryid) REFERENCES categories(id)

