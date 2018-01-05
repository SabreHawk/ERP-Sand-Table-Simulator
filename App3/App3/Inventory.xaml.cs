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
    public sealed partial class Inventory : Page
    {
        public Inventory()
        {
            this.InitializeComponent();
        }
        private void query1_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_production_repository " + yuanliao1.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True") yuanliao1_value.Text = "数量：" + sArray[2];
            else yuanliao1_value.Text = "编号错误";
        }
        private void query2_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_production_repository " + yuanliao2.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True") yuanliao2_value.Text = "数量：" + sArray[2];
            else yuanliao2_value.Text = "编号错误";
        }
        private void query3_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_production_repository " + yuanliao3.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True") yuanliao3_value.Text = "数量：" + sArray[2];
            else yuanliao3_value.Text = "编号错误";
        }



        private void query_1_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_raw_material_repository " + yuanliao_1.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True") yuanliao_1_value.Text = "数量：" + sArray[2];
            else yuanliao_1_value.Text = "编号错误";
        }
        private void query_2_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_raw_material_repository " + yuanliao_2.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True") yuanliao_2_value.Text = "数量：" + sArray[2];
            else yuanliao_2_value.Text = "编号错误";
        }
        private void query_3_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_raw_material_repository " + yuanliao_3.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True") yuanliao_3_value.Text = "数量：" + sArray[2];
            else yuanliao_3_value.Text = "编号错误";
        }
        private void Add_Click(object sender, RoutedEventArgs e)           /////更新产品库存
        {

        }
        private void Add2_Click(object sender, RoutedEventArgs e)          //////更新原料库存
        {
            if (true) return;
        }
    }
}
