CREATE TABLE "UNIVERSITIES" (
  "ID" serial PRIMARY KEY,
  "NAME" varchar UNIQUE,
  "CITY" varchar,
  "COUNTRY" varchar
);

CREATE TABLE "DEPARTMENTS" (
  "ID" serial PRIMARY KEY,
  "FACULTY" varchar,
  "NAME" varchar,
  unique ("FACULTY","NAME")
);

CREATE TABLE "STUDENTS" (
  "ID" serial PRIMARY KEY,
  "EMAIL" varchar UNIQUE,
  "PASSWORD" text,
  "NAME" varchar,
  "DEPARTMANT" int,
  "UNIVERSTY" int,
  "CITY" int,
  FOREIGN KEY ("DEPARTMANT") REFERENCES "DEPARTMENTS" ("ID"),
  FOREIGN KEY ("UNIVERSTY") REFERENCES "UNIVERSITIES" ("ID"),
  FOREIGN KEY ("CITY") REFERENCES "CITIES" ("ID")
);

CREATE TABLE "CITIES" (
  "ID" serial UNIQUE,
  "COUNTRY" varchar,
  "NAME" varchar,
  PRIMARY KEY ("COUNTRY", "NAME")
);

CREATE TABLE "STUDENT_SKILL" (
  "ID" serial,
  "STU_ID" int,
  "SKILL_ID" int,
  PRIMARY KEY ("STU_ID", "SKILL_ID"),
  FOREIGN KEY ("STU_ID") REFERENCES "STUDENTS" ("ID"),
  FOREIGN KEY ("SKILL_ID") REFERENCES "SKILLS" ("ID")
);

CREATE TABLE "COMPANIES" (
  "ID" serial PRIMARY KEY,
  "EMAIL" varchar UNIQUE,
  "PASSWORD" text,
  "NAME" varchar UNIQUE,
  "CITY" int,
  "EXC_ID" int,
  "EXC_NAME" varchar,
  "EXC_DOB" date,
  FOREIGN KEY ("CITY") REFERENCES "CITIES" ("ID")
);

CREATE TABLE "JOB_LISTINGS" (
  "ID" serial PRIMARY KEY,
  "COMPANY" int,
  "DESCRIPTION" varchar,
  "LOCATION" int,
  FOREIGN KEY ("COMPANY") REFERENCES "COMPANIES" ("ID"),
  FOREIGN KEY ("LOCATION") REFERENCES "CITIES" ("ID")
);

CREATE TABLE "JOB_REQ" (
  "ID" serial,
  "JOB_ID" int,
  "REQ_ID" int,
  PRIMARY KEY ("JOB_ID", "REQ_ID"),
  FOREIGN KEY ("JOB_ID") REFERENCES "JOB_LISTINGS" ("ID"),
  FOREIGN KEY ("REQ_ID") REFERENCES "SKILLS" ("ID")
);

CREATE TABLE "SKILLS" (
  "ID" serial PRIMARY KEY,
  "NAME" varchar UNIQUE,
  "DESCRIPTION" varchar
);

CREATE TABLE "APLICATIONS" (
  "JOB_ID" int,
  "STU_ID" int,
  "DIRECTION" boolean,
  "RESPONSE" boolean,
  FOREIGN KEY ("JOB_ID") REFERENCES "JOB_LISTINGS" ("ID"),
  FOREIGN KEY ("STU_ID") REFERENCES "STUDENTS" ("ID")
);
