from cohere_api.healthHarborModel.classificationModel import _get_disease_with_medicine

return_sample = [
    {
        'rank': 1,
        'medicine': 'tynanol',
        'disease': 'headache',
        'confindence': 0.33
    },
    {
        'rank': 2,
        'medicine': 'tynanol',
        'disease': 'headache',
        'confindence': 0.24

    },
    {
        'rank': 3,
        'medicine': 'tynanol',
        'disease': 'headache',
        'confindence': 0.12

    },
]


def get_disease_with_medicine(description: str) -> list[dict[str, str]]:
    return _get_disease_with_medicine(description)
