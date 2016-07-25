DROP TABLE IF EXISTS websitePerf;
create table websitePerf(
    websiteID       integer NOT NULL  primary key  AUTO_INCREMENT,
    websiteAddr     char(255),
    charOrder       integer,
    POST            varchar(255),
    encoding        varchar(20),
    removeTags  varchar(255),
    textXPathKey    varchar(255),
    titleXPathKey   varchar(255),
    indexXPathKey   varchar(255),
    nextCharXPathKey    varchar(255),
    searchXpath varchar(255)
    );


DROP TABLE IF EXISTS books;
create table books(
    bookID  integer NOT NULL primary key AUTO_INCREMENT,
    bkName  varchar(20),
    author  varchar(20),
    indexLink   varchar(255),
    totalCharNum    integer default 0,
    startChar   integer default -1,
    endChar integer default -1
    --  CharNum  integer,
--  CharTitle   varchar(255),
--  CharContect   TEXT,
--  FOREIGN KEY (CharNum) references  CharacterTable,
--  FOREIGN KEY (CharTitle) references  CharacterTable,
--  FOREIGN KEY (CharContext) references  CharactersTable
    );

DROP TABLE IF EXISTS CharactersTable;
create table CharactersTable(
    bookID  integer NOT NULL,
    CharNum  integer NOT NULL,
    CharTitle   varchar(255),
    CharContect   TEXT,
    PRIMARY KEY (bookID,CharNum),
    FOREIGN KEY (bookID) references books(bookID) ON DELETE CASCADE
);

    
    
