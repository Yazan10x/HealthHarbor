import FLASK_HTTPS from "./FLASK_API";
import {HealthItem} from "../Models/HealthItem";


export namespace ItemAPI {

    let route_name = "/health_item"

    export const get_item = async (item_id: string) => {
        return FLASK_HTTPS.get(route_name + "/get_item/" + item_id)
            .then((res) => {
                return res.data as HealthItem
            })
    }

    export const get_items = async (query: any) => {
        return FLASK_HTTPS.get(route_name + "/get_items")
            .then((res) => {
                return res.data as Array<HealthItem>
            })
    }

    export const create_item = async (item: HealthItem) => {
        return FLASK_HTTPS.post(route_name + "/create_item", item)
            .then((res) => {
                return res.data as HealthItem
            })
    }

    export const update_item = async (item: HealthItem) => {
        return FLASK_HTTPS.post(route_name + "/update_item", item)
            .then((res) => {
                return res.data as HealthItem
            })
    }

}
