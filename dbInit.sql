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

drop table if exists user;
-- Each user need their own unique reading process
create table user(
	uid	integer	NOT NULL   AUTO_INCREMENT    primary key,
	passwd	integer,
	email	varchar(100),
    defaultSendingFeq   integer default 24,    -- by hours -> 24 = sending update per day /
    defaultDayTime      Time default '08:00:00',
    salt    TimeStamp   default     CURRENT_TIMESTAMP
);

drop table if exists tasks;
-- Weak Entity of user - used to store user reading process and Sending Time
create table tasks(
	taskID	integer NOT NULL AUTO_INCREMENT,
	bookID	integer NOT NULL,
	uid 	integer NOT NULL,
    startChar   integer default -1,
    endChar integer default -1,
    SendingFeq  integer     default NULL,
    DayTime     integer     default NULL,
    unique(taskID),
    PRIMARY KEY (taskID,uid,bookID),
	FOREIGN key (bookID) REFERENCES books(bookID)ON DELETE CASCADE,
	FOREIGN key (uid) REFERENCES user(uid)ON DELETE CASCADE
);


DROP TRIGGER IF EXISTS `setTaskdefaultToUser`;
create trigger setTaskdefaultToUser
    before insert on tasks
    for each row
begin
        DECLARE defaultSending  integer;
        DECLARE defaultDayTime  Time;
        if (new.SendingFeq = NULL) then
            select defaultSendingFeq into defaultSending from user
            where user.uid = new.uid;
            set new.SendingFeq = defaultSending;
        end if ;
        if (new.SendingFeq = NULL) then
            select defaultSendingFeq into defaultDayTime from user
            where user.uid = new.uid;
            set new.SendingFeq = defaultDayTime;
        end if ;
    end
