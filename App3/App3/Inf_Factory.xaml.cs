using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Navigation;

// https://go.microsoft.com/fwlink/?LinkId=234238 上介绍了“空白页”项模板

namespace App3
{
    /// <summary>
    /// 可用于自身或导航至 Frame 内部的空白页。
    /// </summary>
    public sealed partial class Inf_Factory : Page
    {
        public Inf_Factory()
        {
            this.InitializeComponent();
        }
        private void Chaxun_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_production_order " + cxcpxx.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True")
            {
                bianhao.Text = "编号：" + sArray[1];
                minchen.Text = "名称：" + sArray[2];
                yuanliao.Text = "原料组成:" + sArray[3];
            }
            else
            {
                bianhao.Text = "订单号输入错误";
                minchen.Text = " ";
                yuanliao.Text = "";
            }


        }
        private void Chaxun_1_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_raw_material_order " + cxylxx.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True")
            {
                bianhao_.Text = "编号：" + sArray[1];
                minchen_.Text = "名称：" + sArray[2];
                jiage_.Text = "价格:" + sArray[3];
                jiaohuo_.Text = "交货时间" + sArray[4];
            }
            else
            {
                bianhao.Text = "订单号输入错误";
                minchen.Text = " ";
                jiage_.Text = "";
                jiaohuo_.Text = " ";

            }


        }

    }
}
