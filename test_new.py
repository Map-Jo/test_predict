import pandas as pd
import streamlit as st
import pandas_datareader as pdr


st.title('Korea Stocks π')
Stockcode = pd.read_csv('data/stockcode_pdr.csv')
Stockcode.set_index('name', inplace = True)

Name = st.text_input('μ£Όμμ’λͺ©μλ ₯νμ', placeholder='μμ) μΌμ±μ μ')
Code_name_list = Stockcode.index.tolist()

if Name in Code_name_list:
    code_num = Stockcode.at[Name, 'code']
    code_num = code_num
    # st.text(code_num)
    df = pdr.get_data_yahoo(code_num)
    df['Change'] = df['Close'].tail(2)[0] - df['Close'].tail(2)[1]
    # stock_df
    col1, col2, col3 = st.columns(3)
    col1.metric("νμ¬ μ£Όμκ°κ²©",format(df['Close'].tail(1)[0], ',')+'μ', "%dμ" %(df['Close'].diff().tail(1)[0]))
    col2.metric("νμ¬ κ±°λλ", format(df['Volume'].tail(1)[0], ','),"%.2f%%" %(df['Volume'].pct_change().tail(1)[0] * 100))
    col3.metric("μ μΌ λλΉ κ°κ²©", "%dμ" %(df['Close'].diff().tail(1)[0]), "%.2f%%" %(df['Change'].tail(1)[0] * 100))

elif Name not in Code_name_list:
    st.text('κ²μνμ  μ£Όμ μ’λͺ©μ΄ μμ΅λλ€. μ ννκ² μλ ₯ν΄μ£ΌμΈμ.')

# choice = st.selectbox('κ²μνμ€ μ£Όμ μ’λͺ©λͺμ μλ ₯ν΄ μ£ΌμΈμ.',name_list)
# for i in range(len(name_list)):
#     if choice == name_list[i]:
#         choice_name = Stockcode.loc[Stockcode['Name'] == name_list[i], 'Name'].values
#         choice_name_to_str =np.array2string(choice_name).strip("[]")
#         Name = choice_name_to_str.strip("''")
# Stockcode.set_index('Name', inplace=True)
# Code_name_list = Stockcode.index.tolist()
# with st.spinner('Wait for it...'):
#     if Name in Code_name_list:
#         code_num = Stockcode.at[Name, 'Symbol']
#         df = fdr.DataReader(code_num)
#         col1, col2, col3 = st.columns(3)
#         col1.metric("νμ¬ μ£Όμκ°κ²©",format(df['Close'].tail(1)[0], ',')+'μ', "%dμ" %(df['Close'].diff().tail(1)[0]))
#         col2.metric("νμ¬ κ±°λλ", format(df['Volume'].tail(1)[0], ','),"%.2f%%" %(df['Volume'].pct_change().tail(1)[0] * 100))
#         col3.metric("μ μΌ λλΉ κ°κ²©", "%dμ" %(df['Close'].diff().tail(1)[0]), "%.2f%%" %(df['Change'].tail(1)[0] * 100))
        # fig = px.line(df, y='Close', title='{} μ’κ° Time Series'.format(Name))
        # fig.update_xaxes(
        #     rangeslider_visible=True,
        #     rangeselector=dict(
        #         buttons=list([
        #             dict(count=1, label="1m", step="month", stepmode="backward"),
        #             dict(count=3, label="3m", step="month", stepmode="backward"),
        #             dict(count=6, label="6m", step="month", stepmode="backward"),
        #             dict(step="all")
        #           ])
        #       )
        #   )
        # st.plotly_chart(fig, use_container_width=True)
        # fig2 = go.Figure(data=[go.Candlestick(x=df.index,
        #             open=df['Open'],
        #             high=df['High'],
        #                 low=df['Low'],
        #                 close=df['Close'],
        #                 increasing_line_color = 'tomato',
        #                 decreasing_line_color = 'royalblue',
        #                 showlegend = False)])
        # fig2.update_layout(title='{} Candlestick chart'.format(Name))
        # st.plotly_chart(fig2, use_container_width=True)
    # elif Name not in Code_name_list:
    #     st.text('κ²μνμ  μ£Όμ μ’λͺ©μ΄ μμ΅λλ€. μ ννκ² μλ ₯ν΄μ£ΌμΈμ.')