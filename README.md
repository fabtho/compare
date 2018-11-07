# usage

## url.txt format

 * first line: projectname
 * following lines: urls to grab


### beispiel url.txt

dummy8.taywa.ch.txt:

dummy8.taywa.ch
http://dummy8.taywa.ch/home/
http://dummy8.taywa.ch/weiterbildung/
http://dummy8.taywa.ch/ph-schwyz/
http://dummy8.taywa.ch/ausbildung/kontakte/
http://dummy8.taywa.ch/ausbildung/mentorinnen-und-mentoren/

dannach mit nochmals laufen oder zweite url.txt machen


dummy8neu.taywa.ch.txt

dummy8neu.taywa.ch
http://dummy8neu.taywa.ch/home/
http://dummy8neu.taywa.ch/weiterbildung/
http://dummy8neu.taywa.ch/ph-schwyz/
http://dummy8neu.taywa.ch/ausbildung/kontakte/
http://dummy8neu.taywa.ch/ausbildung/mentorinnen-und-mentoren/


ich habe jeweils dafür eine softlink gemacht

ln -sf dummy8.taywa.ch.txt url.txt

bzw

ln -sf dummy8neu.taywa.ch.txt url.txt


## start
python compare.py

erste beim zweiten lauf werden die unterschiede berrechnet.

## 





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
