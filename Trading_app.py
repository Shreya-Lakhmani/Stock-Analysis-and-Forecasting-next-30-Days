import streamlit as st

st.set_page_config(
    page_title= "Trading App",
    page_icon= "charts_With_downwards_trend:",
    layout= "wide"
)

st.title("Trading Guide App 📊")
st.header("We provide the Greatest Platform for you to collect all information prior to investing in stocks.")
st.image("app.jpg")

st.markdown('## We provide the following services:')

st.markdown("#### :one: Stock Info.")
st.write("Through this page, you cans see all the info. about stock.")


st.markdown("#### :two: Stock Prediction")
st.write("You can explore predicted closing prices for the next 30 Days based on historical stock data and advanced forecasting models. Use this tool to gain valuable insights into market trends and make informed investment decisions")

st.markdown("#### :three: CAPM Return")
st.write("Discover how the Capital Asset Pricing Model(CAPM) calculates the expected return of different stocks asset based on its risk and market performance")
st.write("CAPM indicates that the expected return on a security is equal to the risk-free return plus a risk premium")
st.markdown("$r_i$  = $r_f$ + $B_i$ ($r_m$ - $r_f$)")
st.write("$r_i$ = Expected Return On Security")
st.write("$r_f$ = Risk free rate of return")
st.write("$B_i$ = Beta between the stock and the market")
st.write("$r_m$ = Expected return of the market")
st.markdown("Risk Free Asset Return")
st.write("A risk-free asset return is the rate of return earned on an investment that has no risk of default and no uncertainty in returns.")
st.write("👉 It is the minimum return an investor expects without taking any risk.")
st.markdown("Market Portfolio Return")
st.write("Market Portfolio Return is the return earned by the overall market, represented by a market index that includes all risky assets.")

st.markdown(' #### :four: CAPM Beta')
st.write("Calculates Beta and Expected Return for Individual Stocks.")
st.write("β = 1 : Same risk as market")
st.write("β > 1 : More volatile than market")
st.write("β < 1 : Less volatile than market")
st.write("β = 0 : No market risk (risk-free asset)")
st.write("β < 0 : Moves opposite to market")