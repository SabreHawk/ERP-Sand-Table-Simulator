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
    public sealed partial class Inf_Order : Page
    {
        public Inf_Order()
        {
            this.InitializeComponent();
        }
        private void Chaxun_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_raw_material_order "+Order_num.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True")
            {
                back_value.Text = "";
                id_value.Text = sArray[1];
                name_value.Text = sArray[2];
                yuanliaoid_value.Text = sArray[3];
                shuangliang_value.Text = sArray[4];
                jiaohuoshijian_value.Text = sArray[5];
                dindanriqi_value.Text = sArray[6];
                chanshenriqi_value.Text = sArray[7];
            }
            else
            {
                back_value.Text = "订单号输入错误";
                id_value.Text = "";
                name_value.Text = "";
                yuanliaoid_value.Text = "";
                shuangliang_value.Text = "";
                jiaohuoshijian_value.Text = "";
                dindanriqi_value.Text = "";
                chanshenriqi_value.Text = "";
            }
        }

        private void Chaxun_Click_(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_production_order " + Order_num.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True")
            {
                back_value_.Text = "";
                id_value_.Text = sArray[1];
                name_value_.Text = sArray[2];
                yuanliaoid_value_.Text = sArray[3];
                shuangliang_value_.Text = sArray[4];
                jiaohuoshijian_value_.Text = sArray[5];
            }
            else
            {
                back_value_.Text = "订单号输入错误";
                id_value_.Text = "";
                name_value_.Text = "";
                yuanliaoid_value_.Text = "";
                shuangliang_value_.Text = "";
                jiaohuoshijian_value_.Text = "";
            }
        }



    }
}
