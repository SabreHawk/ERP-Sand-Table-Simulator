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

// https://go.microsoft.com/fwlink/?LinkId=402352&clcid=0x804 上介绍了“空白页”项模板

namespace App3
{
    /// <summary>
    /// 可用于自身或导航至 Frame 内部的空白页。
    /// </summary>
    public sealed partial class MainPage : Page
    {
        public MainPage()
        {
            this.InitializeComponent();
            TitleTextBlock.Text = "信息概览";
            MyFrame.Navigate(typeof(Inf_Summary));
            Inf_Summary.IsSelected = true;
        }

        private void HamburgerButton_Click(object sender,RoutedEventArgs e)
        {
            MySplitView.IsPaneOpen = !MySplitView.IsPaneOpen;
        }

        private void ListBox_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            if(Inf_Summary.IsSelected)
            {
                MyFrame.Navigate(typeof(Inf_Summary));
                TitleTextBlock.Text = "信息概览";
            }
            if (Inf_Factory.IsSelected)
            {
                MyFrame.Navigate(typeof(Inf_Factory));
                TitleTextBlock.Text = "厂房信息";
            }
            if (Inf_Order.IsSelected)
            {
                MyFrame.Navigate(typeof(Inf_Order));
                TitleTextBlock.Text = "订单信息";
            }
            if (Inventory.IsSelected)
            {
                MyFrame.Navigate(typeof(Inventory));
                TitleTextBlock.Text = "产品/原料库存";
            }
        }
    }
}
