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
        private void query4_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_production_repository " + yuanliao4.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True") yuanliao4_value.Text = "数量：" + sArray[2];
            else yuanliao4_value.Text = "编号错误";
        }
        private void query5_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_production_repository " + yuanliao5.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True") yuanliao5_value.Text = "数量：" + sArray[2];
            else yuanliao5_value.Text = "编号错误";
        }
        private void query6_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_production_repository " + yuanliao6.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True") yuanliao6_value.Text = "数量：" + sArray[2];
            else yuanliao6_value.Text = "编号错误";
        }
        private void query7_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_production_repository " + yuanliao7.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True") yuanliao7_value.Text = "数量：" + sArray[2];
            else yuanliao7_value.Text = "编号错误";
        }
        private void query8_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_production_repository " + yuanliao8.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True") yuanliao8_value.Text = "数量：" + sArray[2];
            else yuanliao8_value.Text = "编号错误";
        }
        private void query9_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_production_repository " + yuanliao9.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True") yuanliao9_value.Text = "数量：" + sArray[2];
            else yuanliao9_value.Text = "编号错误";
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
        private void query_4_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_raw_material_repository " + yuanliao_4.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True") yuanliao_4_value.Text = "数量：" + sArray[2];
            else yuanliao_4_value.Text = "编号错误";
        }
        private void query_5_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_raw_material_repository " + yuanliao_5.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True") yuanliao_5_value.Text = "数量：" + sArray[2];
            else yuanliao_5_value.Text = "编号错误";
        }
        private void query_6_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_raw_material_repository " + yuanliao_6.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True") yuanliao_6_value.Text = "数量：" + sArray[2];
            else yuanliao_6_value.Text = "编号错误";
        }
        private void query_7_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_raw_material_repository " + yuanliao_7.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True") yuanliao_7_value.Text = "数量：" + sArray[2];
            else yuanliao_7_value.Text = "编号错误";
        }
        private void query_8_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_raw_material_repository " + yuanliao_8.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True") yuanliao_8_value.Text = "数量：" + sArray[2];
            else yuanliao_8_value.Text = "编号错误";
        }
        private void query_9_Click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_query_raw_material_repository " + yuanliao_9.Text;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True") yuanliao_9_value.Text = "数量：" + sArray[2];
            else yuanliao_9_value.Text = "编号错误";
        }
        private void Add_Click(object sender, RoutedEventArgs e)
        {

        }
        private void Add2_Click(object sender, RoutedEventArgs e)
        {
            if (true) return;
        }
    }
}
