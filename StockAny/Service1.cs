using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Linq;
using System.ServiceProcess;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace WindowsService1
{
    public partial class Service1 : ServiceBase
    {
        System.Timers.Timer timer1;   //计时器
        public Service1()
        {
            InitializeComponent();
        }

        protected override void OnStart(string[] args)
        {
            //用代码生成的
            timer1 = new System.Timers.Timer();
            timer1.Interval = 3000;   //设置计时器事件间隔执行时间
            timer1.Elapsed += new System.Timers.ElapsedEventHandler(timer1_Elapsed);
            timer1.Enabled = true;

            //用控件的
            timer2.Enabled = true;
        }

        protected override void OnStop()
        {
            this.timer1.Enabled = false;
        }

        public static void WriteLog(string path, string strContent)
        {
            FileStream fs;
            if (!File.Exists(path))
                fs = new FileStream(path, FileMode.Create);
            else
                fs = new FileStream(path, FileMode.Append);
            StreamWriter sw = new StreamWriter(fs);
            //开始写入
            sw.WriteLine(strContent);
            //清空缓冲区
            sw.Flush();
            //关闭流
            sw.Close();
            fs.Close();
        }

        public void timer1_Elapsed(object sender, System.Timers.ElapsedEventArgs e)
        {          
            //windows服务中用绝对路径生效
            string strCurPath = "C:\\Users\\Administrator\\Desktop\\Debug\\Log\\" + System.DateTime.Now.ToString("yyyyMMdd") + ".txt";

            WriteLog(strCurPath, System.DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss") + " 测试2:  OK!!!");
        }

        private void timer2_Elapsed(object sender, System.Timers.ElapsedEventArgs e)
        {
            //用相对路径
            string strpath = AppDomain.CurrentDomain.BaseDirectory;
            strpath += "\\Log\\" + System.DateTime.Now.ToString("yyyyMMdd") + ".txt";
            WriteLog(strpath, System.DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss") + " 测试AppDomain.CurrentDomain.BaseDirectory:  OK!!!");
        }
    }
}
