# Experiment backlog and historical questions

Historical observations below are reported, with original evidence pending. The question column defines follow-up work, not an already established resolution.

| Experiment | Reported observation | Next bounded question |
|---|---|---|
| Multiple authoritative CSVs | Mitch Armstrong 401 appeared in duplicate Identity Cubes | What exact naming/correlation/source configuration produced each identity? |
| JDBC identity mapping | Initial Cubes showed employeeID only; later mapping work populated attributes | Which schema/mapping and refresh changes produced each attribute? |
| Business/IT Roles | Assignability and entitlement outcomes differed | Was the IT Role required, permitted, detected, requestable or assigned? |
| Job-title roles | Automatic assignment was investigated | Do assignment and provisioning options produce and remove intended access in this release? |
| Custom form | Empty/blank identity choices appeared | Are filter attribute, value type, allowed values and workflow return mappings correct? |
| Named logging | Expected events were missing | Which config/appender/level and execution branch were active? |
| Conditional Oracle plan | Create plus Modify in one plan was considered | Does the exact connector support all required attributes in Create, or is verified sequential execution needed? |

Record actual failures and controlled retests using the [template](../docs/lab-template.md). Keep source exports private until sanitized and label new reproductions separately from historical originals.
