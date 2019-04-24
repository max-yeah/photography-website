INSERT INTO boss VALUES (1, 'boss', 'Edward Xu', 'edwardxu800422', 35000, '1980-04-22');
INSERT INTO boss VALUES (2, 'boss', 'Michelle Gu', 'michellegu820910', 35000, '1982-09-10');


INSERT INTO boss_phone VALUES (1, '13680042266');
INSERT INTO boss_phone VALUES (1, '86056666');
INSERT INTO boss_phone VALUES (2, '13982091088');
INSERT INTO boss_phone VALUES (2, '86058888');


INSERT INTO projectmanager VALUES (1, 'project manager', 'James Liu', 'jamesliu920101', 'junior', 11000, '1992-01-01', 1);
INSERT INTO projectmanager VALUES (2, 'project manager', 'Mary Chen', 'marychen930202', 'junior', 11000, '1993-02-02', 1);
INSERT INTO projectmanager VALUES (3, 'project manager', 'John Feng', 'johnfeng940303', 'junior', 11000, '1994-03-03', 2);
INSERT INTO projectmanager VALUES (4, 'project manager', 'Linda Wu', 'lindawu930123', 'junior', 11000, '1993-01-23', 2);
INSERT INTO projectmanager VALUES (5, 'project manager', 'Patricia Lin', 'patricialin890404', 'senior', 15000, '1989-04-04', 1);
INSERT INTO projectmanager VALUES (6, 'project manager', 'Robert Zhou', 'robertzhou870505', 'senior', 15000, '1987-05-05', 2);


INSERT INTO projectmanager_phone VALUES (1, '13623478987');
INSERT INTO projectmanager_phone VALUES (1, '86050123');
INSERT INTO projectmanager_phone VALUES (2, '13678923432');
INSERT INTO projectmanager_phone VALUES (2, '86050234');
INSERT INTO projectmanager_phone VALUES (3, '13645632123');
INSERT INTO projectmanager_phone VALUES (3, '86050345');
INSERT INTO projectmanager_phone VALUES (4, '13667834543');
INSERT INTO projectmanager_phone VALUES (4, '86050456');
INSERT INTO projectmanager_phone VALUES (5, '13701023456');
INSERT INTO projectmanager_phone VALUES (5, '86050567');
INSERT INTO projectmanager_phone VALUES (6, '13702034567');
INSERT INTO projectmanager_phone VALUES (6, '86050678');


INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid) VALUES (1, '2019-02-01', 'complete', 14, 688, 'window of the world', 'wedding', 9, 1);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (2, '2019-02-02', 'complete', 21, 988, 'cuhk(sz)', 'art', 8, 5);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (3, '2019-02-04', 'complete', 14, 688, 'happy valley', 'business', 8, 2);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (4, '2019-02-05', 'complete', 7, 388, 'shenzhen bay', 'art', 8, 3);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (5, '2019-02-06', 'complete', 21, 988, 'shenzhen middle school', 'wedding', 9, 6);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (6, '2019-02-06', 'complete', 7, 388, 'xiangmi park', 'wedding', 9, 4);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (7, '2019-02-08', 'complete', 14, 688, 'oct', 'art', 9, 1);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (8, '2019-02-09', 'complete', 14, 688, 'dafen village', 'art', 7, 2);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (9, '2019-02-11', 'complete', 21, 988, 'tencent headquarter', 'business', 8, 5);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (10, '2019-02-11', 'complete', 7, 388, 'coco park', 'wedding', 9, 3);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid) VALUES (11, '2019-03-01', 'after effect', 14, 688, 'window of the world', 'wedding', 9, 1);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (12, '2019-03-02', 'taking photo', 21, 988, 'cuhk(sz)', 'art', 8, 5);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (13, '2019-03-04', 'taking photo', 14, 688, 'happy valley', 'business', 8, 2);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (14, '2019-03-05', 'after effect', 7, 388, 'shenzhen bay', 'art', 8, 3);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (15, '2019-03-06', 'taking photo', 21, 988, 'shenzhen middle school', 'wedding', 9, 6);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (16, '2019-03-06', 'after effect', 7, 388, 'xiangmi park', 'wedding', 9, 4);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (17, '2019-03-08', 'taking photo', 14, 688, 'oct', 'art', 9, 1);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (18, '2019-03-09', 'preparing', 14, 688, 'dafen village', 'art', 7, 2);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (19, '2019-03-11', 'preparing', 21, 988, 'tencent headquarter', 'business', 8, 5);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (20, '2019-03-11', 'preparing', 7, 388, 'coco park', 'wedding', 9, 3);

INSERT INTO photographer VALUES (1, 'photographer', 'Michael Zhang', 'michaelzhang950117', 'junior', 8000, '1995-01-17');
INSERT INTO photographer VALUES (2, 'photographer', 'Barbara Yang', 'barbarayang950208', 'junior', 8000, '1995-02-08');
INSERT INTO photographer VALUES (3, 'photographer', 'William Li', 'williamli960325', 'junior', 8000, '1996-03-25');
INSERT INTO photographer VALUES (4, 'photographer', 'Elizabeth Xia', 'elizabethxia940407', 'junior', 8000, '1994-04-07');
INSERT INTO photographer VALUES (5, 'photographer', 'David Ma', 'davidma940516', 'junior', 8000, '1994-05-16');
INSERT INTO photographer VALUES (6, 'photographer', 'Jennifer Luo', 'jenniferluo920623', 'senior', 12000, '1992-06-23');
INSERT INTO photographer VALUES (7, 'photographer', 'Richard Song', 'richardsong910709', 'senior', 12000, '1991-07-09');
INSERT INTO photographer VALUES (8, 'photographer', 'Maria Shen', 'mariashen900811', 'senior', 12000, '1990-08-11');


INSERT INTO photographer_phone VALUES (1, '13601171234');
INSERT INTO photographer_phone VALUES (2, '13702082345');
INSERT INTO photographer_phone VALUES (3, '13803253456');
INSERT INTO photographer_phone VALUES (4, '13904074567');
INSERT INTO photographer_phone VALUES (5, '13605165678');
INSERT INTO photographer_phone VALUES (6, '13706236789');
INSERT INTO photographer_phone VALUES (7, '13807097890');
INSERT INTO photographer_phone VALUES (8, '13908118901');


INSERT INTO takephoto VALUES (1, 1);
INSERT INTO takephoto VALUES (1, 2);
INSERT INTO takephoto VALUES (2, 6);
INSERT INTO takephoto VALUES (2, 3);
INSERT INTO takephoto VALUES (2, 4);
INSERT INTO takephoto VALUES (3, 5);
INSERT INTO takephoto VALUES (3, 1);
INSERT INTO takephoto VALUES (4, 2);
INSERT INTO takephoto VALUES (5, 7);
INSERT INTO takephoto VALUES (5, 3);
INSERT INTO takephoto VALUES (5, 4);
INSERT INTO takephoto VALUES (6, 5);
INSERT INTO takephoto VALUES (7, 1);
INSERT INTO takephoto VALUES (7, 2);
INSERT INTO takephoto VALUES (8, 3);
INSERT INTO takephoto VALUES (8, 4);
INSERT INTO takephoto VALUES (9, 8);
INSERT INTO takephoto VALUES (9, 5);
INSERT INTO takephoto VALUES (9, 1);
INSERT INTO takephoto VALUES (10, 2);


INSERT INTO aftereffect VALUES (1, 'after effect', 'Charles An', 'charlesan950909', 'junior', 6000, '1995-09-09');
INSERT INTO aftereffect VALUES (2, 'after effect', 'Susan Bao', 'susanbao961018', 'junior', 6000, '1996-10-18');
INSERT INTO aftereffect VALUES (3, 'after effect', 'Joseph Cai', 'josephcai951125', 'junior', 6000, '1995-11-25');
INSERT INTO aftereffect VALUES (4, 'after effect', 'Margaret Deng', 'margaretdeng1230', 'junior', 6000, '1996-12-30');
INSERT INTO aftereffect VALUES (5, 'after effect', 'Thomas Fang', 'thomasfang940127', 'junior', 6000, '1994-01-27');
INSERT INTO aftereffect VALUES (6, 'after effect', 'Dorothy Gao', 'dorothygao890213', 'senior', 9000, '1989-02-13');
INSERT INTO aftereffect VALUES (7, 'after effect', 'Christopher Han', 'christopherhan880304', 'senior', 9000, '1988-03-04');
INSERT INTO aftereffect VALUES (8, 'after effect', 'Lisa Jiang', 'lisajiang900430', 'senior', 9000, '1990-04-30');


INSERT INTO aftereffect_phone VALUES (1, '13609094321');
INSERT INTO aftereffect_phone VALUES (2, '13710185432');
INSERT INTO aftereffect_phone VALUES (3, '13811256543');
INSERT INTO aftereffect_phone VALUES (4, '13912307654');
INSERT INTO aftereffect_phone VALUES (5, '13601278765');
INSERT INTO aftereffect_phone VALUES (6, '13702139876');
INSERT INTO aftereffect_phone VALUES (7, '13803040987');
INSERT INTO aftereffect_phone VALUES (8, '13904301098');


INSERT INTO doeffect VALUES (1, 4);
INSERT INTO doeffect VALUES (1, 5);
INSERT INTO doeffect VALUES (2, 8);
INSERT INTO doeffect VALUES (2, 2);
INSERT INTO doeffect VALUES (2, 3);
INSERT INTO doeffect VALUES (3, 1);
INSERT INTO doeffect VALUES (3, 4);
INSERT INTO doeffect VALUES (4, 5);
INSERT INTO doeffect VALUES (5, 7);
INSERT INTO doeffect VALUES (5, 2);
INSERT INTO doeffect VALUES (5, 3);
INSERT INTO doeffect VALUES (6, 1);
INSERT INTO doeffect VALUES (7, 4);
INSERT INTO doeffect VALUES (7, 5);
INSERT INTO doeffect VALUES (8, 2);
INSERT INTO doeffect VALUES (8, 3);
INSERT INTO doeffect VALUES (9, 6);
INSERT INTO doeffect VALUES (9, 1);
INSERT INTO doeffect VALUES (9, 4);
INSERT INTO doeffect VALUES (10, 5);


INSERT INTO devicemanager VALUES (1, 'device manager', 'Daniel Kang', 'danielkang960531', 'junior', 5000, '1996-05-31');
INSERT INTO devicemanager VALUES (2, 'device manager', 'Paul Liu', 'paulliu950622', 'junior', 5000, '1995-06-22');
INSERT INTO devicemanager VALUES (3, 'device manager', 'Mark Meng', 'markmeng920716', 'senior', 8000, '1992-07-16');


INSERT INTO devicemanager_phone VALUES (1, '13605316666');
INSERT INTO devicemanager_phone VALUES (2, '13706227777');
INSERT INTO devicemanager_phone VALUES (3, '13807168888');
