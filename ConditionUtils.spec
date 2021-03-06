/*
A KBase module: ConditionUtils
*/
#include <KBaseExperiments.spec>
module ConditionUtils {

    typedef int bool;

    /* @id ws KBaseExperiments.ConditionSet */
    typedef string ws_condition_set_id;

    /* @id ws KBaseExperiments.ClusterSet */
    typedef string ws_cluster_set_id;

    /*
        Get condition information in a friendly format

        ws_condition_set_id condition_set_ref
        list<string> conditions - Optional: Which conditions should be returned. defaults to all conditions in the set

        Returns {condition_label: {ontology_type(e.g. GO): [Factors]}}

    */

    typedef structure {
        ws_condition_set_id condition_set_ref;
        list<string> conditions;
    } GetConditionParams;

    typedef structure {
        mapping<string, mapping<string, list<KBaseExperiments.Factor>>> conditions;
    } GetConditionOutput;

    funcdef get_conditions(GetConditionParams params)
        returns (GetConditionOutput result) authentication required;

    /*
        input_shock_id and input_file_path - alternative input params,
    */
    typedef structure {
        string input_shock_id;
        string input_file_path;
        string output_ws_id;
        string output_obj_name;
    } FileToConditionSetParams;

    typedef structure {
        ws_condition_set_id condition_set_ref;
    } FileToConditionSetOutput;

    funcdef file_to_condition_set(FileToConditionSetParams params)
        returns (FileToConditionSetOutput result) authentication required;

    typedef structure {
        ws_condition_set_id input_ref;
        string destination_dir;
    } ConditionSetToTsvFileParams;

    typedef structure {
        string file_path;
    } ConditionSetToTsvFileOutput;

    funcdef condition_set_to_tsv_file(ConditionSetToTsvFileParams params)
        returns (ConditionSetToTsvFileOutput result) authentication required;

    typedef structure {
        ws_condition_set_id input_ref;
    } ExportConditionSetParams;

    typedef structure {
        ws_cluster_set_id input_ref;
    } ExportClusterSetParams;

    typedef structure {
        string shock_id;
    } ExportOutput;

    funcdef export_condition_set_tsv(ExportConditionSetParams params)
        returns (ExportOutput result) authentication required;

    funcdef export_condition_set_excel(ExportConditionSetParams params)
        returns (ExportOutput result) authentication required;

    funcdef export_cluster_set_excel(ExportClusterSetParams params)
        returns (ExportOutput result) authentication required;

};
