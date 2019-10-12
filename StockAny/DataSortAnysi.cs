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
                    if (Convert.ToDouble(dtCode.Rows[iCode]["收"].ToString()) - Convert.ToDouble(dtCode.Rows[iCode]["开"].ToString()) <= 0)
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
                    label1.Text = "序列表:" + dt.Rows[i][0].ToString() + " | " + i.ToString() + " | " + string.Format("{0:d}", dtCode.Rows[0]["ddate"].ToString());
                }
                Application.DoEvents();
            }

        }

        private void DataSortAnysi_Load(object sender, EventArgs e)
        {
            dateTimePicker1.Value = DateTime.Now;
        }


        //当日涨幅大于8的，后3天累计涨幅
        private void button5_Click(object sender, EventArgs e)
        {
            textBox3.Text = "";

            string strSqlCmd = " select  * from [" + textBox4.Text.Trim() + "] " +
                               "  order by ddate asc";
            DataTable dtStock = SQLLibary.QryData(strSqlCmd).Tables[0];
            if (dtStock.Rows.Count > 1)
            {
                textBox3.AppendText("涨" + textBox2.Text + "% 后" + textBox5.Text + "天的涨幅");
                textBox3.AppendText("\r\n");
                for (int iDay = 0; iDay < dtStock.Rows.Count; iDay++)
                {
                    double DFirstOpen = Convert.ToDouble(dtStock.Rows[iDay]["开"].ToString());
                    double DFirstClose = Convert.ToDouble(dtStock.Rows[iDay]["收"].ToString());

                    //统计 涨
                    if (((DFirstClose / DFirstOpen) - 1) * 100 >= Convert.ToInt32(textBox2.Text.Trim()))
                    {
                        //string aa = (((DFirstClose / DFirstOpen) - 1) * 100).ToString();
                        //MessageBox.Show(aa);
                        try
                        {
                            int iLastDays = Convert.ToInt32(textBox5.Text.Trim().ToString());
                            double DThreeClose = Convert.ToDouble(dtStock.Rows[iDay + iLastDays]["收"].ToString());
                            double TotalPercent = ((DThreeClose / DFirstClose) - 1) * 100;

                            //MessageBox.Show(DThreeClose.ToString() + "  " + DFirstClose.ToString());

                            textBox3.AppendText(TotalPercent.ToString() + "   " + Convert.ToDateTime(dtStock.Rows[iDay]["ddate"].ToString()).ToShortDateString());
                            textBox3.AppendText("\r\n");
                        }
                        catch { }
                    }
                    label1.Text = "序列表:" + textBox4.Text.Trim() + " | " + iDay.ToString() + " | " + Convert.ToDateTime(dtStock.Rows[iDay]["ddate"].ToString()).ToShortDateString();
                }

                textBox3.AppendText("\r\n");
                textBox3.AppendText("跌" + textBox2.Text + "% 后" + textBox5.Text + "天的涨幅");
                textBox3.AppendText("\r\n");

                for (int iDay = 0; iDay < dtStock.Rows.Count; iDay++)
                {
                    double DFirstOpen = Convert.ToDouble(dtStock.Rows[iDay]["开"].ToString());
                    double DFirstClose = Convert.ToDouble(dtStock.Rows[iDay]["收"].ToString());

                    //统计 跌
                    if (((DFirstClose / DFirstOpen) - 1) * 100 <= -Convert.ToInt32(textBox2.Text.Trim()))
                    {
                        try
                        {
                            int iLastDaysDown = Convert.ToInt32(textBox5.Text.Trim().ToString());
                            double DThreeCloseDown = Convert.ToDouble(dtStock.Rows[iDay + iLastDaysDown]["收"].ToString());
                            double TotalPercentDown = ((DThreeCloseDown / DFirstClose) - 1) * 100;

                            
                            textBox3.AppendText(TotalPercentDown.ToString() + "   " + Convert.ToDateTime(dtStock.Rows[iDay]["ddate"].ToString()).ToShortDateString());
                            textBox3.AppendText("\r\n");
                        }
                        catch { }
                    }
                }
            }
            Application.DoEvents();
        }

        //分析涨跌平均
        private void button6_Click(object sender, EventArgs e)
        {
            textBox3.Text = "";

            string strSqlCmd = " select top " + textBox6.Text.Trim() + " * from [" + textBox4.Text.Trim() + "] " +
                               "  order by ddate desc";
            DataTable dtStock = SQLLibary.QryData(strSqlCmd).Tables[0];
            if (dtStock.Rows.Count > 1)
            {
                double DUp = 0;
                int iUp = 0;
                double DDown = 0;
                int iDown = 0;

                int iotoone = 0;
                int ionetothree = 0;
                int ithreetofive = 0;
                int ifivetosever = 0;
                int iserverup = 0;

                int iDotoone = 0;
                int iDonetothree = 0;
                int iDthreetofive = 0;
                int iDfivetosever = 0;
                int iDserverup = 0;

                for (int iDay = 0; iDay < dtStock.Rows.Count; iDay++)
                {
                    double DFirstOpen = Convert.ToDouble(dtStock.Rows[iDay]["开"].ToString());
                    double DFirstClose = Convert.ToDouble(dtStock.Rows[iDay]["收"].ToString());

                    if (DFirstClose >= DFirstOpen)
                    {
                        DUp += ((DFirstClose / DFirstOpen) - 1) * 100;
                        iUp++;
                    }
                    else
                    {
                        DDown += ((DFirstClose / DFirstOpen) - 1) * 100;
                        iDown++;
                    }

                    double DTradeDay = ((DFirstClose / DFirstOpen) - 1) * 100;

                    if (DTradeDay >= 0 && DTradeDay < 1)
                        iotoone++;
                    if (DTradeDay >= 1 && DTradeDay < 3)
                        ionetothree++;
                    if (DTradeDay >= 3 && DTradeDay < 5)
                        ithreetofive++;
                    if (DTradeDay >= 5 && DTradeDay < 7)
                        ifivetosever++;
                    if (DTradeDay >= 7)
                        iserverup++;

                    if (DTradeDay < 0 && DTradeDay >= -1)
                        iDotoone++;
                    if (DTradeDay < -1 && DTradeDay >= -3)
                        iDonetothree++;
                    if (DTradeDay < -3 && DTradeDay >= -5)
                        iDthreetofive++;
                    if (DTradeDay < -5 && DTradeDay >= -7)
                        iDfivetosever++;
                    if (DTradeDay < -7)
                        iDserverup++;


                    label1.Text = "序列表:" + textBox4.Text.Trim() + " | " + iDay.ToString() + " | " + Convert.ToDateTime(dtStock.Rows[iDay]["ddate"].ToString()).ToShortDateString();
                }

                textBox3.AppendText("上涨总百分比 " + Math.Round(DUp,2).ToString() + "   上涨总天数  " + iUp.ToString());
                textBox3.AppendText("\r\n");
                textBox3.AppendText("上涨平均 " + Math.Round(((DUp / iUp)),2).ToString());
                textBox3.AppendText("\r\n");

                textBox3.AppendText("下跌总百分比 " + Math.Round(DDown,2).ToString() + "   下跌总天数  " + iDown.ToString());
                textBox3.AppendText("\r\n");
                textBox3.AppendText("下跌平均 " + Math.Round(((DDown / iDown)),2).ToString());
                textBox3.AppendText("\r\n");
                textBox3.AppendText("---------------------");
                textBox3.AppendText("\r\n");

                //分段统计涨跌幅
                textBox3.AppendText("上涨0～1  " + iotoone.ToString()+" 天");
                textBox3.AppendText("\r\n");
                textBox3.AppendText("上涨1～3  " + ionetothree.ToString() + " 天");
                textBox3.AppendText("\r\n");
                textBox3.AppendText("上涨3～5  " + ithreetofive.ToString() + " 天");
                textBox3.AppendText("\r\n");
                textBox3.AppendText("上涨5～7  " + ifivetosever.ToString() + " 天");
                textBox3.AppendText("\r\n");
                textBox3.AppendText("上涨7～  " + iserverup.ToString() + " 天");
                textBox3.AppendText("\r\n");
                textBox3.AppendText("\r\n");

                textBox3.AppendText("下跌0～1  " + iDotoone.ToString() + " 天");
                textBox3.AppendText("\r\n");
                textBox3.AppendText("下跌1～3  " + iDonetothree.ToString() + " 天");
                textBox3.AppendText("\r\n");
                textBox3.AppendText("下跌3～5  " + iDthreetofive.ToString() + " 天");
                textBox3.AppendText("\r\n");
                textBox3.AppendText("下跌5～7  " + iDfivetosever.ToString() + " 天");
                textBox3.AppendText("\r\n");
                textBox3.AppendText("下跌7～  " + iDserverup.ToString() + " 天");
                textBox3.AppendText("\r\n");

            }
            Application.DoEvents();

        }
    }
}
