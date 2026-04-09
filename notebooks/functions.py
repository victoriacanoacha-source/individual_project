import pycountry

def format_columns(df: pd.DataFrame, rename_dict: dict = None, keep_columns: list = None) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[^\w\s]", "", regex=True)
        .str.replace(" ", "_"))
    if rename_dict:
        df = df.rename(columns=rename_dict)
    if keep_columns:
        df = df[keep_columns]
    return df

def check_null(df):
    nulls = df.isna().sum()
    percent = (nulls / len(df)) * 100
    return pd.DataFrame({
        "missing_values": nulls,
        "percent_missing": percent})


def assign_phase(year):
    if year <= 2001:
        return "Early Globalisation"
    if year <= 2008:
        return "Hyper-globalisation"
    if year <= 2017:
        return "Post-financial crisis adjustment"
    if year <= 2018:
        return "Geopolitical fragmentation"
    if year <= 2021:
        return "Global supply chain shock"
    else:
        return "Strategic diversification"
        



def main_supplier_by_country_year(df):
    data = df.copy()
    totals = data.groupby(["importer", "year"])["trade_value"].transform("sum")
    data["supplier_share"] = data["trade_value"] / totals

    idx = data.groupby(["importer", "year"])["supplier_share"].idxmax()

    result = data.loc[idx, [
        "importer",
        "year",
        "exporter",
        "trade_value",
        "supplier_share"
    ]].copy()

    result = result.rename(columns={"exporter": "main_supplier"})

    return result.sort_values(["importer", "year"])




def get_iso3(country):
    try:
        return pycountry.countries.lookup(country).alpha_3
    except:
        return None