/* init table for database tables and potentially their checks */

CREATE TABLE location (
    LID integer primary key,
    address varchar[500],
    country varchar[100]
);

CREATE TABLE customer (
    CID integer primary key,
    LID integer references location(LID),
    name varchar[100],
    email varchar[100]
);

CREATE TABLE department (
    DepID integer primary key,
    LID integer references location(LID),
    name varchar[100]
);

CREATE TABLE project (
    PrID integer primary key,
    CID integer references customer(CID),
    name varchar[100],
    budget money,
    startDate date,
    deadline date
);

CREATE TABLE employee (
    EmpID integer primary key,
    DepID integer references department(DepID),
    name varchar[100],
    email varchar[100]
);

CREATE TABLE userGroup (
    GrID integer primary key,
    name varchar[100]
);

CREATE TABLE role (
    RoleID integer primary key,
    name varchar[100]
);

/* project - employee */
CREATE TABLE works (
    PrID integer references project(PrID),
    EmpID integer references employee(EmpID),
    started date
);

/* employee - usergroup */
CREATE TABLE partOf (
    EmpID integer references employee(EmpID),
    GrID integer references userGroup(GrID)
);

/* employee - role */
CREATE TABLE has (
    RoleID integer references role(RoleID),
    EmpID integer references employee(EmpID),
    description text
);
