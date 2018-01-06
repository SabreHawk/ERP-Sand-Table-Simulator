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
    public sealed partial class Inf_Summary : Page
    {
        public Inf_Summary()
        {
            this.InitializeComponent();
        }
        private void produce_click(object sender, RoutedEventArgs e)
        {
            string chaxun = "sys_produce " + id_.Text + " " + num_.Text ;

            string result = SystemManager.UploadAndDownload(chaxun);
            string[] sArray = result.Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            if (sArray[0] == "True")
            {
                back_value.Text = "成功！";
            }
            else
            {
                back_value.Text = "失败！";
            }


        }
    }
}
