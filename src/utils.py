import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


def execute_plt_code(code: str, df: pd.DataFrame):
    """Execute the passing code to plot figure

    Args:
        code (str): action string (containing plt code)
        df (pd.DataFrame): our dataframe

    Returns:
        _type_: plt figure
    """

    try:
        local_vars = {"plt": plt, "df": df}
        compiled_code = compile(code, "<string>", "exec")
        exec(compiled_code, globals(), local_vars)

        return plt.gcf()

    except Exception as e:
        st.error(f"Error excuting plt code: {e}")
        return None
