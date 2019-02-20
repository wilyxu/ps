using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace StockAny
{
    public partial class DataSortAnysi : Form
    {
        public DataSortAnysi()
        {
            InitializeComponent();
        }
        QHZY SQLLibary = new QHZY();


        //n个交易日小碎步上涨
        private void button1_Click(object sender, EventArgs e)
        {
            //n个交易日小碎步上涨
            string strTradeDay = textBox1.Text;

            string strSystemCode = "select * from SystemCode ";
            DataTable dt = SQLLibary.QryData(strSystemCode).Tables[0];
            for (int i = 0; i < dt.Rows.Count; i++)
            {
                //if (dt.Rows[i][0].ToString() == "000922")
                //    MessageBox.Show("aa");
                string strSqlCmd = " select top " + strTradeDay + " * from [" + dt.Rows[i][0].ToString() + "] where 1=1 order by ddate desc";//and ddate<='2017-02-15'
                DataTable dtCode = SQLLibary.QryData(strSqlCmd).Tables[0];

                bool bIsChoosed = true;
                if (dtCode.Rows.Count < 3) bIsChoosed = false;
                for (int iCode = 0; iCode < dtCode.Rows.Count; iCode++)
                {
                    if (Convert.ToDouble(dtCode.Rows[iCode]["收"].ToString()) - Convert.ToDouble(dtCode.Rows[iCode]["开"].ToString())<=0)
                    {
                        bIsChoosed = false;
                    }                    
                }

                label1.Text = "序列表:" + dt.Rows[i][0].ToString() + " | " + i.ToString();
                if (bIsChoosed)
                    listBox1.Items.Add(dt.Rows[i][0].ToString());

                Application.DoEvents();
            }
        }

        //20日均线之上
        //5日均线刚上穿20日
        private void button2_Click(object sender, EventArgs e)
        {
            string strSystemCode = "select * from SystemCode ";
            DataTable dt = SQLLibary.QryData(strSystemCode).Tables[0];
            for (int i = 0; i < dt.Rows.Count; i++)
            {
                string strSqlCmd = " select top 20 * from [" + dt.Rows[i][0].ToString() + "] order by ddate desc";
                DataTable dtCode = SQLLibary.QryData(strSqlCmd).Tables[0];
                if (dtCode.Rows.Count > 0)
                {
                    double fSumFinalValue20 = 0;
                    double fSumFinalValue5 = 0;
                    for (int iSum = 0; iSum < dtCode.Rows.Count; iSum++)
                    {
                        fSumFinalValue20 += Convert.ToDouble(dtCode.Rows[iSum]["收"].ToString());

                        if (iSum < 5) fSumFinalValue5 += Convert.ToDouble(dtCode.Rows[iSum]["收"].ToString());
                    }

                    fSumFinalValue20 = fSumFinalValue20 / 20;
                    fSumFinalValue5 = fSumFinalValue5 / 5;

                    if (Convert.ToDouble(dtCode.Rows[0]["收"].ToString()) > fSumFinalValue20 && (fSumFinalValue5 - fSumFinalValue20) / fSumFinalValue20 > 0.001 && (fSumFinalValue5 - fSumFinalValue20) / fSumFinalValue20 < 0.01)
                        listBox1.Items.Add(dt.Rows[i][0].ToString());
                }

                label1.Text = "序列表:" + dt.Rows[i][0].ToString() + " | " + i.ToString();
                Application.DoEvents();
            }
        }

        //按股价找股
        private void button3_Click(object sender, EventArgs e)
        {
            string strSystemCode = "select * from SystemCode ";
            DataTable dt = SQLLibary.QryData(strSystemCode).Tables[0];
            for (int i = 0; i < dt.Rows.Count; i++)
            {
                string strSqlCmd = " select  * from [" + dt.Rows[i][0].ToString() + "] where 1=1 and ddate='2017-04-25' order by ddate desc";//and ddate<='2017-02-15'
                DataTable dtCode = SQLLibary.QryData(strSqlCmd).Tables[0];

                bool bIsChoosed = false;

                if (dtCode.Rows.Count > 0)
                {
                    if (dtCode.Rows[0]["收"].ToString() == "32.38")
                    {
                        bIsChoosed = true;
                    }
                }

                label1.Text = "序列表:" + dt.Rows[i][0].ToString() + " | " + i.ToString();
                if (bIsChoosed)
                    listBox1.Items.Add(dt.Rows[i][0].ToString());

                Application.DoEvents();
            }

        }

        //长阴十字
        private void button4_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            string strSystemCode = "select * from SystemCode ";
            DataTable dt = SQLLibary.QryData(strSystemCode).Tables[0];
            for (int i = 0; i < dt.Rows.Count; i++)
            {
                string strSqlCmd = " select top 2 * from [" + dt.Rows[i][0].ToString() + "] " +
                                   "  where ddate<= '" + dateTimePicker1.Value + "' " +
                                   "  order by ddate desc";
                DataTable dtCode = SQLLibary.QryData(strSqlCmd).Tables[0];
                if (dtCode.Rows.Count > 1)
                {
                    double DBigDownClose = Convert.ToDouble(dtCode.Rows[1]["收"].ToString());
                    double DBigDownOpen = Convert.ToDouble(dtCode.Rows[1]["开"].ToString());
                    double DCrossClose = Convert.ToDouble(dtCode.Rows[0]["收"].ToString());
                    double DCrossOpen = Convert.ToDouble(dtCode.Rows[0]["开"].ToString());
                    double DCrossHigh = Convert.ToDouble(dtCode.Rows[0]["高"].ToString());
                    double DCrossLow = Convert.ToDouble(dtCode.Rows[0]["低"].ToString());

                    double VolBigDown = Convert.ToDouble(dtCode.Rows[1]["量"].ToString());
                    double VolCross = Convert.ToDouble(dtCode.Rows[0]["量"].ToString());

                    if (DBigDownClose < DBigDownOpen && DCrossClose > DCrossOpen)
                    {
                        double BigDownPercent = (DBigDownOpen - DBigDownClose) / DBigDownOpen;
                        double CrossPercent = (DCrossClose - DCrossOpen) / DCrossOpen;

                        //长阴4个点以上，小红十字
                        if (BigDownPercent > 0.03 && BigDownPercent <= 0.0812 && CrossPercent > 0.001 && CrossPercent < 0.01)
                        {
                            if (DCrossHigh - DCrossClose < DCrossOpen - DCrossLow)
                            {
                                if (checkBox1.Checked)
                                {
                                    if (VolCross > VolBigDown)
                                        listBox1.Items.Add(dt.Rows[i][0].ToString());
                                }
                                else
                                {
                                    listBox1.Items.Add(dt.Rows[i][0].ToString());
                                }
                            }
                        }

                    }
                    label1.Text = "序列表:" + dt.Rows[i][0].ToString() + " | " + i.ToString() + " | " + string.Format("{0:d}",dtCode.Rows[0]["ddate"].ToString());
                }
                Application.DoEvents();
            }

        }

        private void DataSortAnysi_Load(object sender, EventArgs e)
        {
            dateTimePicker1.Value = DateTime.Now;
        }


    }
}
