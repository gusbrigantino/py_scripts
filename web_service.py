from zeep import Client

client = Client(wsdl='https://montereycsp.netsmartcloud.com/csp/montereyuat/avcws/WEBSVC.DCIImport.cls?WSDL=1')

sysCode = "UAT"
userName = "BRIGANTINOG"
passwrd = "19FRIEDCHICKEN1938?"

DCIImportFileWarnings = 1

resultStream = ""

DCIImportRecord = "<?xml version=\"1.0\"?>"
DCIImportRecord = DCIImportRecord + "<option>"
DCIImportRecord = DCIImportRecord + "<optionidentifier>USER261</optionidentifier>"
DCIImportRecord = DCIImportRecord + "<optiondata>"
DCIImportRecord = DCIImportRecord + "<FACILITY>1</FACILITY>"
DCIImportRecord = DCIImportRecord + "<PATID>1</PATID>"
DCIImportRecord = DCIImportRecord + "<SYSTEM.MC_tx_plan_audit>"
DCIImportRecord = DCIImportRecord + "   <tx_plan_name>TESTPLAN</tx_plan_name>"
DCIImportRecord = DCIImportRecord + "   <recorded_date>01/19/2021</recorded_date>"
DCIImportRecord = DCIImportRecord + "   <tx_plan_length>150</tx_plan_length>"
DCIImportRecord = DCIImportRecord + "   <tx_plan_link>link</tx_plan_link>"
DCIImportRecord = DCIImportRecord + "   <tx_plan_sequence>99</tx_plan_sequence>"
DCIImportRecord = DCIImportRecord + "   <tx_plan_date>01/19/2021</tx_plan_date>"
DCIImportRecord = DCIImportRecord + "   <staff_name>Brigantino</staff_name>"
DCIImportRecord = DCIImportRecord + "   <tx_plan_consent_record>N</tx_plan_consent_record>"
DCIImportRecord = DCIImportRecord + "   <No_Consent_Reasons>GM</No_Consent_Reasons>"
DCIImportRecord = DCIImportRecord + "</SYSTEM.MC_tx_plan_audit>"
DCIImportRecord = DCIImportRecord + "</optiondata>"
DCIImportRecord = DCIImportRecord + "</option>"

recordStream = DCIImportRecord

result = client.service.ImportRecord(sysCode, userName, passwrd, DCIImportRecord, DCIImportFileWarnings, recordStream, resultStream)

print(result)