# usage

## url.txt format

first line: projectname
following lines: urls to grap

## start
python compare.py



## sql statement to get recursivly id

### on domain

SELECT CONCAT(uid, ",") FROM `pages` where hidden = 0 and deleted = 0 and doktype = 1

### multidomain


set @pid = 367;
SELECT uid FROM `pages` where pid = @pid AND hidden = 0 and deleted = 0;
SELECT uid FROM `pages` where pid in (SELECT uid FROM `pages` where pid = @pid AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0;
SELECT uid FROM `pages` where pid in (SELECT uid FROM `pages` where pid in (SELECT uid FROM `pages` where pid = @pid AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0

level 4

SELECT uid FROM `pages` where pid in (SELECT uid FROM `pages` where pid in (SELECT uid FROM `pages` where pid in (SELECT uid FROM `pages` where pid = 175 AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0


SELECT uid FROM `pages` where pid in (SELECT uid FROM `pages` where pid in (SELECT uid FROM `pages` where pid in (SELECT uid FROM `pages` where pid = @pid AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0

set @pid = 367;

# pid

pid taxomex = 367
parkomatic.ch 2

SELECT uid FROM `pages` where pid = 175 AND hidden = 0 and deleted = 0 OR pid in (SELECT uid FROM `pages` where pid = 175 AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0 OR pid in (SELECT uid FROM `pages` where pid in (SELECT uid FROM `pages` where pid = 175 AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0 OR pid in (SELECT uid FROM `pages` where pid in (SELECT uid FROM `pages` where pid in (SELECT uid FROM `pages` where pid = 175 AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0

pid vonballmos 175

global.vonballmos = 283

level 4

OR pid in (SELECT uid FROM `pages` where pid = 175 AND hidden = 0 and deleted = 0 pid in (SELECT uid FROM `pages` where pid in (SELECT uid FROM `pages` where pid = 175 AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0;




(SELECT uid FROM `pages` where pid = 175 AND hidden = 0 and deleted = 0 OR pid in (SELECT uid FROM `pages` where pid = 175 AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0 OR pid in (SELECT uid FROM `pages` where pid in (SELECT uid FROM `pages` where pid = 175 AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0) OR pid in (SELECT uid FROM `pages` where pid in (SELECT uid FROM `pages` where pid = 175 AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0) AND hidden = 0 and deleted = 0)
