import FLASK_HTTPS from "./FLASK_API";
import {MedicineEntry} from "../Models/MedicineEntries";

export namespace CohereAPI {

    let route_name = "/cohere"

    export const get_medicine = async (description: string) => {
        return FLASK_HTTPS.post(route_name + "/get_medicine", {
            description: description
        })
            .then((res) => {
                return res.data as Array<MedicineEntry>
            })
    }

}
