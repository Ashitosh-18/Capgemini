using System;
using System.Collections.Generic;

namespace ProductCatch
{
    // IAccount Interface defining account properties
    public interface IAccount
    {
        DateTime TransactionDate { get; }
        int Cr { get; set; }
        int Dr { get; set; }
        string Particulars { get; set; }

        bool GetAccountInfo();
    }

    // IAccountService Interface defining account operations
    public interface IAccountService
    {
        void AddAccount(IAccount account);
        void UpdateAccount(IAccount account);
        void DeleteAccount(IAccount account);
        List<IAccount> GetAccounts();
    }

    // FinAccount class implementing IAccount and IAccountService
    public class FinAccount : IAccount, IAccountService
    {
        public int Cr { get; set; }
        public int Dr { get; set; }
        public string? Particulars { get; set; }
        public DateTime TransactionDate { get; set; }

        // List to store accounts
        private List<IAccount> accounts = new List<IAccount>();

        // Method to return formatted account info
        public string GetAccountInfo()
        {
            return $"Transaction Date: {TransactionDate}, Credit: {Cr}, Debit: {Dr}, Particulars: {Particulars}";
        }

        // Add an account to the list
        public void AddAccount(IAccount account)
        {
            accounts.Add(account);
            Console.WriteLine("Account added successfully.");
        }

        // Update an account if it exists
        public void UpdateAccount(IAccount account)
        {
            var existingAccount = accounts.Find(a => a.TransactionDate == account.TransactionDate);
            if (existingAccount != null)
            {
                existingAccount.Cr = account.Cr;
                existingAccount.Dr = account.Dr;
                existingAccount.Particulars = account.Particulars;
                Console.WriteLine("Account updated successfully.");
            }
            else
            {
                Console.WriteLine("Account not found.");
            }
        }

        // Delete an account if it exists
        public void DeleteAccount(IAccount account)
        {
            if (accounts.Remove(account))
            {
                Console.WriteLine("Account deleted successfully.");
            }
            else
            {
                Console.WriteLine("Account not found.");
            }
        }

        // Return the list of accounts
        public List<IAccount> GetAccounts()
        {
            return accounts;
        }

        bool IAccount.GetAccountInfo()
        {
            throw new NotImplementedException();
        }
    }

    // Main Program class
    class Program
    {
        static void Main()
        {
            // Create an instance of FinAccount
            FinAccount accountManager = new FinAccount();

            // Create a new account
            IAccount account1 = new FinAccount
            {
                Cr = 1000,
                Dr = 200,
                Particulars = "Salary Credit",
                TransactionDate = DateTime.Now
            };

            // Add the account
            accountManager.AddAccount(account1);
            Console.WriteLine("Account Information:");
            Console.WriteLine(account1.GetAccountInfo());

            // Display all accounts
            Console.WriteLine("\nAll Accounts:");
            foreach (var acc in accountManager.GetAccounts())
            {
                Console.WriteLine(acc.GetAccountInfo());
            }

            // Create another account
            IAccount account2 = new FinAccount
            {
                Cr = 500,
                Dr = 100,
                Particulars = "Utility Bill Payment",
                TransactionDate = DateTime.Now.AddDays(-1)
            };

            // Add second account
            accountManager.AddAccount(account2);

            // Display all accounts again
            Console.WriteLine("\nUpdated Account List:");
            foreach (var acc in accountManager.GetAccounts())
            {
                Console.WriteLine(acc.GetAccountInfo());
            }
        }
    }
}
