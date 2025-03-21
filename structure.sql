CREATE TABLE "core_current_version" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(120) NOT NULL,
    "features" varchar(120) NOT NULL,
    "changes" text NOT NULL,
    "date_creation" datetime NOT NULL,
    "date_update" datetime NOT NULL,
    "deleted" bool NOT NULL
)
CREATE TABLE "core_cfdi_provider" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(100) NOT NULL,
    "user" varchar(240) NOT NULL,
    "authorization" varchar(240) NOT NULL,
    "url" varchar(240) NOT NULL,
    "technical_contact" varchar(240) NOT NULL,
    "phone_contact" varchar(40) NOT NULL,
    "email_contact" varchar(240) NOT NULL,
    "date_creation" datetime NOT NULL,
    "date_update" datetime NOT NULL,
    "deleted" bool NOT NULL
)
CREATE TABLE "core_company" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "company_key" varchar(128) NOT NULL,
    "company_name" varchar(100) NOT NULL,
    "rfc" varchar(40) NOT NULL,
    "date_creation" datetime NOT NULL,
    "date_update" datetime NOT NULL,
    "photo" varchar(100) NOT NULL,
    "deleted" bool NOT NULL,
    "id_current_version_id" integer NULL REFERENCES "core_current_version" ("id") DEFERRABLE INITIALLY DEFERRED
)
CREATE TABLE "core_branch" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "branch_key" varchar(128) NOT NULL,
    "name" varchar(100) NOT NULL,
    "phone" varchar(40) NOT NULL,
    "email" varchar(240) NOT NULL,
    "date_creation" datetime NOT NULL,
    "date_update" datetime NOT NULL,
    "conf_ip_ext" varchar(40) NOT NULL,
    "conf_ip_int" varchar(40) NULL,
    "conf_user" varchar(40) NOT NULL,
    "conf_pass" varchar(40) NOT NULL,
    "conf_db" varchar(80) NOT NULL,
    "conf_port" varchar(80) NULL,
    "photo" varchar(100) NOT NULL,
    "deleted" bool NOT NULL,
    "address" varchar(500) NOT NULL,
    "lat" varchar(50) NULL,
    "long" varchar(50) NULL,
    "id_company_id" integer NOT NULL REFERENCES "core_company" ("id") DEFERRABLE INITIALLY DEFERRED,
    "id_cfdi_provider_id" integer NULL REFERENCES "core_cfdi_provider" ("id") DEFERRABLE INITIALLY DEFERRED
)
CREATE TABLE "customers_customer" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(100) NOT NULL,
    "phone" varchar(40) NOT NULL,
    "email" varchar(240) NOT NULL,
    "address" varchar(500) NOT NULL,
    "country" varchar(100) NOT NULL,
    "state" varchar(100) NOT NULL,
    "city" varchar(100) NOT NULL,
    "zip_code" varchar(20) NOT NULL,
    "company_name" varchar(100) NOT NULL,
    "rfc" varchar(40) NOT NULL,
    "lat" varchar(50) NULL,
    "long" varchar(50) NULL,
    "photo" varchar(100) NOT NULL,
    "date_creation" datetime NOT NULL,
    "date_update" datetime NOT NULL,
    "deleted" bool NOT NULL,
    "id_branch_id" integer NOT NULL REFERENCES "core_branch" ("id") DEFERRABLE INITIALLY DEFERRED,
    "tax_regime" varchar(5) NOT NULL,
    "bill_require" bool NOT NULL,
    "correct_billing_info" bool NOT NULL
)
CREATE TABLE "products_category" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(100) NOT NULL,
    "date_creation" datetime NOT NULL,
    "date_update" datetime NOT NULL,
    "deleted" bool NOT NULL,
    "id_branch_id" integer NULL REFERENCES "core_branch" ("id") DEFERRABLE INITIALLY DEFERRED,
    "id_current_version_id" integer NULL REFERENCES "core_current_version" ("id") DEFERRABLE INITIALLY DEFERRED,
    "description" varchar(500) NOT NULL
)
CREATE TABLE "products_product" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(100) NOT NULL,
    "description" text NULL,
    "price" decimal NOT NULL,
    "stock" integer unsigned NOT NULL CHECK ("stock" >= 0),
    "date_creation" datetime NOT NULL,
    "date_update" datetime NOT NULL,
    "category_id" integer NULL REFERENCES "products_category" ("id") DEFERRABLE INITIALLY DEFERRED,
    "deleted" bool NOT NULL
)
CREATE TABLE "invoices_invoice" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "date_sale" date NOT NULL,
    "total" decimal NOT NULL,
    "total_taxes" decimal NOT NULL,
    "state" varchar(20) NOT NULL,
    "date_creation" datetime NOT NULL,
    "date_update" datetime NOT NULL,
    "deleted" bool NOT NULL,
    "id_customer_id" integer NULL REFERENCES "customers_customer" ("id") DEFERRABLE INITIALLY DEFERRED
)
CREATE TABLE "invoices_invoicedetail" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "total" decimal NOT NULL,
    "total_taxes" decimal NOT NULL,
    "date_creation" datetime NOT NULL,
    "date_update" datetime NOT NULL,
    "deleted" bool NOT NULL,
    "id_invoice_id" integer NULL REFERENCES "invoices_invoice" ("id") DEFERRABLE INITIALLY DEFERRED,
    "id_product_id" integer NULL REFERENCES "products_product" ("id") DEFERRABLE INITIALLY DEFERRED,
    "quantity" decimal NOT NULL
)