DEFINE TABLE a2a_handoff SCHEMAFULL;

DEFINE FIELD source_agent ON TABLE a2a_handoff TYPE string;
DEFINE FIELD target_agent ON TABLE a2a_handoff TYPE string;
DEFINE FIELD workflow_id ON TABLE a2a_handoff TYPE string;
DEFINE FIELD run_id ON TABLE a2a_handoff TYPE string;
DEFINE FIELD intent ON TABLE a2a_handoff TYPE object;
DEFINE FIELD task ON TABLE a2a_handoff TYPE object;
DEFINE FIELD context ON TABLE a2a_handoff TYPE object;
DEFINE FIELD environment ON TABLE a2a_handoff TYPE object;
DEFINE FIELD knowledge ON TABLE a2a_handoff TYPE object;
DEFINE FIELD capabilities ON TABLE a2a_handoff TYPE object;
DEFINE FIELD permissions ON TABLE a2a_handoff TYPE object;
DEFINE FIELD mode ON TABLE a2a_handoff TYPE string;
DEFINE FIELD status ON TABLE a2a_handoff TYPE string;
DEFINE FIELD result ON TABLE a2a_handoff FLEXIBLE TYPE option<object>;
DEFINE FIELD error ON TABLE a2a_handoff FLEXIBLE TYPE option<string>;
DEFINE FIELD created_at ON TABLE a2a_handoff TYPE datetime VALUE time::now();
DEFINE FIELD updated_at ON TABLE a2a_handoff TYPE datetime VALUE time::now();

DEFINE INDEX a2a_handoff_run_idx ON TABLE a2a_handoff FIELDS run_id;
DEFINE INDEX a2a_handoff_status_idx ON TABLE a2a_handoff FIELDS status;
DEFINE INDEX a2a_handoff_target_idx ON TABLE a2a_handoff FIELDS target_agent, status;
