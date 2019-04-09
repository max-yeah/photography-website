DROP TABLE IF EXISTS 
aftereffect, 
aftereffect_phone,  
boughtby,           
 computer,           
 customer,           
 customer_phone,     
 devicemanager,      
 devicemanager_phone, 
 doeffect,    
 photodevice,  
 photographer,
 photographer_phone,
 porder,
 projectmanager,
 projectmanager_phone,
 takephoto,
 vehicle;

-- This will be delected in future version
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS user;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(20) UNIQUE NOT NULL,
  password VARCHAR(100) NOT NULL,
  position VARCHAR(20) UNIQUE
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title VARCHAR(20) NOT NULL,
  body VARCHAR(1000) NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

-- For ManagerLevel: junior, senior, etc
CREATE TABLE projectmanager
(
  id INT NOT NULL AUTO_INCREMENT,
  position VARCHAR(20) NOT NULL,
  username VARCHAR(20) NOT NULL,
  password VARCHAR(100) NOT NULL,
  level VARCHAR(20) NOT NULL DEFAULT '0',
  salary INT NOT NULL DEFAULT 0,
  birthday DATE NOT NULL DEFAULT '2000-01-01',
  PRIMARY KEY (id)
);

CREATE TABLE projectmanager_phone
(
  managerid INT NOT NULL,
  phone VARCHAR(11) NOT NULL,
  PRIMARY KEY (phone, managerid),
  FOREIGN KEY (managerid) REFERENCES projectmanager(id)
);

-- For ordertype: A, B, C, etc
-- One manager can manage multiple orders
-- One order can only be managed by one manager
CREATE TABLE porder
(
  orderid INT NOT NULL,
  startdate DATE NOT NULL,
  expectduration INT NOT NULL,
  price INT NOT NULL,
  place VARCHAR(40) NOT NULL,
  ordertype CHAR(1) NOT NULL,
  satisfaction INT NOT NULL,
  managerid INT NOT NULL,
  PRIMARY KEY (orderid),
  FOREIGN KEY (managerid) REFERENCES projectmanager(id)
);

-- For photographerLevel: junior, senior, etc
CREATE TABLE photographer
(
  id INT NOT NULL AUTO_INCREMENT,
  position VARCHAR(20) NOT NULL,
  username VARCHAR(20) NOT NULL,
  password VARCHAR(100) NOT NULL,
  level VARCHAR(20) NOT NULL DEFAULT '0',
  salary INT NOT NULL DEFAULT 0,
  birthday DATE NOT NULL DEFAULT '2000-01-01',
  PRIMARY KEY (id)
);

CREATE TABLE photographer_phone
(
  photographerid INT NOT NULL,
  phone VARCHAR(11) NOT NULL,
  PRIMARY KEY (phone, photographerid),
  FOREIGN KEY (photographerid) REFERENCES photographer(id)
);

CREATE TABLE takephoto
(
  orderid INT NOT NULL,
  photographerid INT NOT NULL,
  PRIMARY KEY (orderid, photographerid),
  FOREIGN KEY (orderid) REFERENCES porder(orderid),
  FOREIGN KEY (photographerid) REFERENCES photographer(id)
);

-- For EffectLevel: junior, senior, etc
CREATE TABLE aftereffect
(
  id INT NOT NULL AUTO_INCREMENT,
  position VARCHAR(20) NOT NULL,
  username VARCHAR(20) NOT NULL,
  password VARCHAR(100) NOT NULL,
  level VARCHAR(20) NOT NULL DEFAULT '0',
  salary INT NOT NULL DEFAULT 0,
  birthday DATE NOT NULL DEFAULT '2000-01-01',
  PRIMARY KEY (id)
);

CREATE TABLE aftereffect_phone
(
  effectid INT NOT NULL,
  phone VARCHAR(11) NOT NULL,
  PRIMARY KEY (phone, effectid),
  FOREIGN KEY (effectid) REFERENCES aftereffect(id)
);

CREATE TABLE doeffect
(
  orderid INT NOT NULL,
  effectid INT NOT NULL,
  PRIMARY KEY (orderid, effectid),
  FOREIGN KEY (orderid) REFERENCES porder(orderid),
  FOREIGN KEY (effectid) REFERENCES aftereffect(id)
);

-- For gender: M / F
CREATE TABLE customer
(
  customerid INT NOT NULL,
  customerName VARCHAR(20) NOT NULL,
  gender CHAR(1) NOT NULL,
  birthday DATE NOT NULL,
  PRIMARY KEY (customerid)
);

CREATE TABLE customer_phone
(
  customerid INT NOT NULL,
  phone VARCHAR(11) NOT NULL,
  PRIMARY KEY (phone, customerid),
  FOREIGN KEY (customerid) REFERENCES customer(customerid)
);

CREATE TABLE boughtby
(
  orderid INT NOT NULL,
  customerid INT NOT NULL,
  PRIMARY KEY (orderid, customerid),
  FOREIGN KEY (orderid) REFERENCES porder(orderid),
  FOREIGN KEY (customerid) REFERENCES customer(customerid)
);

-- For size: five-seat, seven-seat, etc
-- One vehicle can only be used by one order
-- Some vehicles may not be used by any order
CREATE TABLE vehicle
(
  vehicleid INT NOT NULL,
  size VARCHAR(20) NOT NULL,
  price INT NOT NULL,
  orderid INT,
  PRIMARY KEY (vehicleid),
  FOREIGN KEY (orderid) REFERENCES porder(orderid)
);

CREATE TABLE devicemanager
(
  id INT NOT NULL AUTO_INCREMENT,
  position VARCHAR(20) NOT NULL,
  username VARCHAR(20) NOT NULL,
  password VARCHAR(100) NOT NULL,
  level VARCHAR(20) NOT NULL DEFAULT '0',
  salary INT NOT NULL DEFAULT 0,
  birthday DATE NOT NULL DEFAULT '2000-01-01',
  PRIMARY KEY (id)
);

CREATE TABLE devicemanager_phone
(
  devicemanagerid INT NOT NULL,
  phone VARCHAR(11) NOT NULL,
  PRIMARY KEY (phone, devicemanagerid),
  FOREIGN KEY (devicemanagerid) REFERENCES devicemanager(id)
);

CREATE TABLE photodevice
(
  deviceid INT NOT NULL,
  devicecompany VARCHAR(40) NOT NULL,
  price INT NOT NULL,
  devicestatus VARCHAR(20) NOT NULL,
  boughtdate DATE NOT NULL,
  devicename VARCHAR(40) NOT NULL,
  orderid INT,
  devicemanagerid INT NOT NULL,
  PRIMARY KEY (deviceid),
  FOREIGN KEY (orderid) REFERENCES porder(orderid),
  FOREIGN KEY (devicemanagerid) REFERENCES devicemanager(id)
);

CREATE TABLE computer
(
  computerid INT NOT NULL,
  price INT NOT NULL,
  performance VARCHAR(20) NOT NULL,
  boughtdate DATE NOT NULL,
  devicemanagerid INT NOT NULL,
  PRIMARY KEY (computerid),
  FOREIGN KEY (devicemanagerid) REFERENCES devicemanager(id)
);
