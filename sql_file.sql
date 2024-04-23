
use dcc_assignment_4;
alter table purchase_data rename column `Bond_Number` to bond_number;
alter table political_party_data rename column `Bond_Number` to bond_number;

alter table purchase_data
add column YEAR INT;


SET SQL_SAFE_UPDATES = 0;

