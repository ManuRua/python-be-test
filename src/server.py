from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/turnover/byAgeAndGender")
def getTurnoverByAgeAndGender():
    """
    Accumulated widget: Total turnover & turnovers by age and gender
    Map: Postal code selection

    Keyword arguments:
    startMonth - Filtered by Month when starts the period
    endMonth - Filtered by Month when finishes the period
    postalCode - Filtered by postal code selected
    ordered - Results ordered by turnover [ASC, DESC]
    Return: Total turnover & turnover by age and gender between period
    """
    return jsonify({
        "total": 0,
        "ages": {
            "<=24": {
                "M": 0,
                "F": 0
            },
            "25-34": {
                "M": 0,
                "F": 0
            },
            "35-44": {
                "M": 0,
                "F": 0
            },
            "45-54": {
                "M": 0,
                "F": 0
            },
            "55-64": {
                "M": 0,
                "F": 0
            },
            ">=65": {
                "M": 0,
                "F": 0
            }
        }
    })


@app.route("/turnover/monthlyBy/<field>/")
def turnoverByAgeAndGender(field):
    """
    Time series widget: Monthly turnover by Age or Gender

    Keyword arguments:
    field - Attribute which filter the result [age, gender]
    startMonth - Month when starts the period
    endMonth - Month when finishes the period

    Return: Turnover by age or gender grouped by months between period
    """
    byGender = {
        "2015-01": {
            "M": 0,
            "F": 0
        },
        "2015-02": {
            "M": 0,
            "F": 0
        },
        "2015-03": {
            "M": 0,
            "F": 0
        },
        "2015-04": {
            "M": 0,
            "F": 0
        }
    }
    byAge = {
        "2015-12": {
            "<=24": 0,
            "25-34": 0,
            "35-44": 0,
            "45-54": 0,
            "55-64": 0,
            ">=65": 0
        },
        "2016-01": {
            "<=24": 0,
            "25-34": 0,
            "35-44": 0,
            "45-54": 0,
            "55-64": 0,
            ">=65": 0
        },
        "2016-02": {
            "<=24": 0,
            "25-34": 0,
            "35-44": 0,
            "45-54": 0,
            "55-64": 0,
            ">=65": 0
        },
        "2016-03": {
            "<=24": 0,
            "25-34": 0,
            "35-44": 0,
            "45-54": 0,
            "55-64": 0,
            ">=65": 0
        }
    }
    return jsonify(byGender if field == 'gender' else byAge)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)
