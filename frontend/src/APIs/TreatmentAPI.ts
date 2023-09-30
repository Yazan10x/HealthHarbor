import FLASK_HTTPS from "./FLASK_API";
import {Treatment} from "../Models/Treatment";


export namespace TreatmentAPI {

    let route_name = "/treatments"

    export const get_treatment = async (treatment_id: string) => {
        return FLASK_HTTPS.get(route_name + "/get_treatment/" + treatment_id)
            .then((res) => {
                return res.data as Treatment
            })
    }

    export const get_treatment_by_label = async (treatment_label: string) => {
        return FLASK_HTTPS.get(route_name + "/get_treatment_by_label/" + treatment_label)
            .then((res) => {
                return res.data as Treatment
            })
    }

    export const get_treatments = async (query: any) => {
        return FLASK_HTTPS.post(route_name + "/get_treatments", query)
            .then((res) => {
                return res.data as Array<Treatment>
            })
    }

    export const create_treatment = async (treatment: Treatment) => {
        return FLASK_HTTPS.post(route_name + "/create_treatment", treatment)
            .then((res) => {
                return res.data as Treatment
            })
    }

    export const update_treatment = async (treatment: Treatment) => {
        return FLASK_HTTPS.post(route_name + "/update_treatment", treatment)
            .then((res) => {
                return res.data as Treatment
            })
    }

    export const delete_treatment = async (treatment_id: string) => {
        return FLASK_HTTPS.post(route_name + "/delete_treatment/" + treatment_id)
            .then((res) => {
                return res.data as boolean
            })
    }

}
